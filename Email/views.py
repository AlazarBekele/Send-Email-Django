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

            send_mail (
                form.cleaned_data['FirstName', 'LastName'],
                form.cleaned_data[f"TO:"+'From'],
                form.cleaned_data['MainMessage']
            )

            return redirect ('index')

    context = {
        'form' : form
    }

    return render (request, 'index.html', context=context)