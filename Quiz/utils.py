import random
from .models import EmailOtp
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import os
from dotenv import load_dotenv
load_dotenv()
def generate_otp():
    return str(random.randint(100000,999999))

def send_otp_mail(email,username):
    otp = generate_otp()
    EmailOtp.objects.create(email=email,otp=otp)
    subject = "Your OTP Code for Quiz App Registration"
    from_email=os.environ.get('from_email')
    to_email = email
    context={
        'username':username,
        'otp': otp,
    }

    
    html_content = render_to_string('email_template.html', context)
    text_content = f'Hello {username}, your OTP is {otp}. It expires in 10 minutes.'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
def send_reset_mail(email,username):
    otp = generate_otp()
    EmailOtp.objects.create(email=email,otp=otp)
    subject = "Your OTP Code for Password Reset for Quiz App"
    from_email=os.environ.get('from_email')
    to_email = email
    context={
        'username':username,
        'otp': otp,
        'is_reset': True,
    }    
    html_content = render_to_string('email_template.html', context)
    text_content = f'Hello {username}, your OTP is {otp}. It expires in 10 minutes.'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()