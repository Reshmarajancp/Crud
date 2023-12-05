from django import forms
from work.models import book_models,product_model,stud_model,work


class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.IntegerField()
    contact=forms.IntegerField()

class Book_Form(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    publication_year=forms.IntegerField()
    genre=forms.CharField()

class product_form(forms.ModelForm):
    class Meta:
        model=product_model
        fields=['price','type']

class stud_form(forms.ModelForm):
    class Meta:
        model=stud_model
        fields='__all__'

class work_form(forms.ModelForm):
    class Meta:
        model=work
        fields='__all__'