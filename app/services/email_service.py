import random
from django.conf import settings
from django.core.mail import send_mail
from datetime import timezone


def generate_and_send_otp(author):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    author.otp = otp
    author.otp_sent_at = timezone.now()
    author.save()
    subject = 'Verify Email'
    message = f'Your One-Time Password (OTP) is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [author.email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
    return otp
