from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse


def email(request):
    subject = "Why Chicken Wings Are Delicious"
    message = "crispy, tasty, tiny == delicious"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["d_kearney@bellaliant.net"]
    send_mail(subject, message, email_from, recipient_list)

    return HttpResponse("email sent")
