from django.core.mail import send_mail
from django.shortcuts import render
from ceciliapt.forms import MessageForm


# Create your views here.


def index(request, *args, **kwargs):
    if request.method == "POST":
        mail(request)
        return render(request, "thanks.html", {})
    else:
        return render(request, "index.html", {})


def mail(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            # SETUP COM O EMAIL DA CECILIA TODO
            message = request.POST['name'] + ' ' + '(' + request.POST['email'] + ') diz: ' + request.POST['message']
            send_mail('Mensagem de ' + request.POST['name'], message, 'ceciliaptwebsite@gmail.com',
                      [request.POST['email']])
