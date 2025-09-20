from termios import OPOST
from django.shortcuts import render, redirect
from .forms import EmailFill
from django.core.mail import send_mail

# Create your views here.

def index (request):

    #EmailSend

    form = EmailFill()

    if request.method == 'POST':

        form = EmailFill(request.POST)

        if form.is_valid():

            FullName = form.cleaned_data['FullName'],
            Message = form.cleaned_data['MainMessage']
            From = form.cleaned_data['From']


            send_mail (
                FullName,
                Message,
                From,
                ['To']
            )

            return redirect ('Index')

    context = {
        'form' : form
    }

    return render (request, 'index.html', context=context)