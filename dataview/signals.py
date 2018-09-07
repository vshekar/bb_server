from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(user_logged_in)
def reset_token(sender, **kwargs):
    print("resetting key...")
    token = Token.objects.get(user=kwargs['user'])
    print("Token before : {}".format(token))
    token.key = None
    token.save()
    print("Token after : {}".format(token))
    print(sender.username)

#user_logged_in.connect(reset_token)