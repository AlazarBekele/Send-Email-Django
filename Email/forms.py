from django import forms

class EmailFill (forms.Form):

    FirstName = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name'
    }))

    LastName = forms.CharField (max_length=20, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last Name'
    }))


    From = forms.EmailField (widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'example@gmail.com'
    }))

    MainMessage = forms.CharField (widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Discribe What On Your Mind'
    }))