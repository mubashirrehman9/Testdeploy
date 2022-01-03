
from celery import shared_task
from time import sleep
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_mail_task(email, token):
    subject = 'celery task'
    message = f'Please click on the given link verify your password http://127.0.0.1:8000/registration/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return None