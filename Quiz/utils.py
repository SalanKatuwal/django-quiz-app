import random
from .models import EmailOtp
from django.core.mail import send_mail
import os

def generate_otp():
    return str(random.randint(100000,999999))

import os
def send_otp_mail(email):
    otp = generate_otp()
    EmailOtp.objects.create(email=email,otp=otp)
    
    send_mail(
        subject= "Your Otp code",
        message=f'Your otp for registration on quiz app is {otp}. It expires in 10 minutes',
        from_email=os.environ.get('from_email'),
        recipient_list=[email],
        fail_silently=False,
    )
    