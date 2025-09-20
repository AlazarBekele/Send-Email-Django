from django import forms

class EmailFill (forms.Form):

    FirstName = forms.CharField (label='',max_length=20, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name'
    }))

    LastName = forms.CharField (label='',max_length=20, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last Name'
    }))


    From = forms.EmailField (label='',widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'example@gmail.com'
    }))

    MainMessage = forms.CharField (label='',widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Discribe What On Your Mind'
    }))