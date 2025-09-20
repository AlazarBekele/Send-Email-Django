from django import forms

class EmailFill (forms.Form):

    FullName = forms.CharField (label='',max_length=20, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name'
    }))

    From = forms.EmailField (label='',widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'From: Exmple@gmail.com'
    }))

    To = forms.EmailField (label='',widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'TO: Sample@gmail.com'
    }))

    MainMessage = forms.CharField (label='',widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Discribe What On Your Mind'
    }))