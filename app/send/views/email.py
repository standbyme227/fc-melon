from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render

__all__ = (
    'send_email',
)


def send_email(request):
    # set api key, api secret
    if request.method == 'POST':
        sender = settings.EMAIL_HOST_USER
        is_vaild=True
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipients = []

        recipient = request.POST.get('recipient')
        recipients.append(recipient)

        send_mail(subject, message, sender, recipients)
        #recipients는 list여야 한다.

        # return redirect()
    return render(request, 'send/email.html')
