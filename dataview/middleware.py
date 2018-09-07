from dataview.signals import reset_token
from django.http import HttpResponseForbidden
from dataview.models import LoggedInUser
from django.contrib.auth import logout

class OneSessionPerUserMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            reset_token(user=request.user)
            print("This is when the token is reset")
            all_logged_in = LoggedInUser.objects.all().count()
            if all_logged_in > 1:
                response = HttpResponseForbidden(request)
                logout(request)
            
                

        
        return response