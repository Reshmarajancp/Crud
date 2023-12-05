from django import forms

class Formname(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    Number=forms.IntegerField()

class newform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()

class Emiform(forms.Form):
    loan_amount=forms.IntegerField()
    tenure=forms.IntegerField()
    interest=forms.IntegerField()

class signup(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

class signin(forms.Form):
    uname=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    Reenter_password=forms.CharField(widget=forms.PasswordInput)
