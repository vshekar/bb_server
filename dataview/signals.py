from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from dataview.models import LoggedInUser

#@receiver(user_logged_in)
def reset_token(**kwargs):
    print("resetting key...")
    token = Token.objects.get(user=kwargs['user'])
    print("Token before : {}".format(token))
    token.delete()
    token = Token.objects.create(user= kwargs['user'])
    token.save()
    print("Token after : {}".format(token))
    

#user_logged_in.connect(reset_token)

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    print("This is when the signal gets processed")
    LoggedInUser.objects.get_or_create(user=kwargs.get('user')) 


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()