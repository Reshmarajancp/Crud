from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm
from work.models import Emp
from work.forms import Book_Form,product_form,stud_form,work_form
from work.models import book_models,product_model,stud_model,work

# Create your views here

class Employee(View):
     def get(self,request):
          form=EmpForm()
          return render(request,"add.html",{"form":form})
     
     def post(self,request):
          form=EmpForm(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
               Emp.objects.create(**form.cleaned_data)
               form=EmpForm()
               # modelname.objects.create(values)
               return render(request,"add.html",{"form":form})
          else:
               return render(request,"add.html",{"form":form})
         

class Books(View):
     def get(self,request):
          form=Book_Form()
          return render(request,"year.html",{"form":form})
     def post(self,request):
          form=Book_Form(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
               book_models.objects.create(**form.cleaned_data)
               form=Book_Form()
               return render(request,"year.html",{"form":form})
          else:
               return render(request,"year.html",{"form":form})
          
class product_view(View):
     def get(self,request):
          form=product_form()
          return render(request,"product.html",{"form":form})
     def post(self,request):
          form=product_form(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
               # product_model.objects.create(**form.cleaned_data) # data basilottu data add cheyyan
               form.save()
               # form.save()==product_model.objects.create(**form.cleaned_data)
               form=product_form()
               return render(request,"product.html",{"form":form})
          else:
               return render(request,"product.html",{"form":form})

class product_list(View):
     def get(self,requset):
          qs=product_model.objects.all()
          return render(requset,"pro_list.html",{"qs":qs})
     
class work_view(View):
     def get(self,request):
          form=work_form()
          return render(request,"workers.html",{"form":form})
     def post(self,request):
          form=work_form(request.POST)
          if form.is_valid():
               print(form.changed_data)
               form.save()
               form=work_form()
               return render(request,"workers.html",{"form":form})
          else:
               return render(request,"workers.html",{"form":form})

class working_list(View):
     def get(self,request):
          qs=work.objects.all()
          return render(request,"workers_list.html",{"qs":qs})
          
class stud_view(View):
     def get(self,request):
          form=stud_form()
          return render(request,"student.html",{"form":form})
     def post(self,request):
          form=stud_form(request.POST)
          if form.is_valid():
               print(form.changed_data)
               form.save()
               form=stud_form()
               return render(request,"student.html",{"form":form})
          else:
               return render(request,"student.html",{"form":form})

class stud_list(View):
     def get(self,request):
          qs=stud_model.objects.all()
          return render(request,"stud_list.html",{"qs":qs})

class stud_list_view(View):
     def get(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          qs=stud_model.objects.get(id=id)
          return render(request,"students.html",{"data":qs})

class stud_delete(View):
     def get(self,request,*args,**kwargs):
          id=kwargs.get("pk")
          stud_model.objects.get(id=id).delete()
          return redirect('stud-all')


     
