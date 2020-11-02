from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from ceciliapt.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
from ceciliapt.forms import MessageForm


# Create your views here.
from mainapp.models import Message


def index(request, *args, **kwargs):
    if request.method == "POST":
        message(request)
        return render(request, "thanks.html", {})
    else:
        print(request.LANGUAGE_CODE)
        if request.LANGUAGE_CODE == 'pt':
            return render(request, "index-pt.html", {})
        else:
            return render(request, "index-en.html", {})

'''
def mail(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # SETUP COM O EMAIL DA CECILIA TODO
            message = request.POST['name'] + ' ' + '(' + request.POST['email'] + ') diz: ' + request.POST['message']
            send_mail('Mensagem de ' + request.POST['name'], EMAIL_HOST_USER,
                      [request.POST['email']], False, EMAIL_HOST_PASSWORD, html_message=message)
    else:
        return HttpResponse("<header>Unavailable</header>")
'''

def message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            ip = visitor_ip_address(request)
            name = request.POST['name']
            email = request.POST['email']
            msg = request.POST['message']
            m = Message(ip, name, email, msg, timezone.now())
            m.save()


def visitor_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
