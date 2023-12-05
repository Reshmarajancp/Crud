from django.shortcuts import render
from django.views.generic import View
from operation.forms import Formname,newform,Emiform,signup,signin


class FormView(View):
    def get(self,request):
        form = Formname() # form enna variablilekk Forname ennathine koduthu bcz Formname ennath oru class aahn(forms.py il und aah claa)
        return render(request,"form.html",{"form":form})
    def post(self,request):
        print(request.POST)
        form=Formname(request.POST) # igane kodukkumbol athil values keri nikkum
        if form.is_valid():
            print("myname",form.cleaned_data["name"])
            print("email",form.cleaned_data["email"])
            print("address",form.cleaned_data["address"])
            print("password",form.cleaned_data["password"])
            print("Number",form.cleaned_data["Number"])
            form=Formname() # again igane kodukkumbol kodutha values ellam submit cheyyumbol form blank aavum
        else:
            print("good by")
        return render(request,"form.html",{"form":form})
    
class newview(View):
    def get(self,request):
        formm=newform
        return render(request,"f.html",{"formm":formm})
    def post(self,request):
        print(request.POST)
        formm=newform(request.POST)
        if formm.is_valid():
            print("name",formm.cleaned_data["name"])
            print("email",formm.cleaned_data["email"])
        else:
            print("quite")
        return render(request,"f.html",{"formm":formm})
    
class Emiview(View):
    def get(self,request):
        form=Emiform()
        return render(request,"emi.html",{"form":form})
    def post(self,request):
        form=Emiform(request.POST)
        if form.is_valid():
            print("loan amount : ",form.cleaned_data["loan_amount"])
            print("tenure      : ",form.cleaned_data["tenure"])
            print("interest    : ",form.cleaned_data["interest"])
            
            
                             #   OR
            # print(form.cleaned_data)
            # loan_amount=form.cleaned_data.get("loan_amount")
            # tenure=form.cleaned_data.get("tenure")
            # interest=form.cleaned_data.get("interest")   
            # form=Emiform()
            # n=tenure*12
            # r=interest
            # p=loan_amount
            # emi=p*r*(1+r)**n/((1+r)**n-1)

            
        else:
            print("leave it")
        return render(request,"emi.html",{"form":form})

class Signup(View):
    def get(self,request):
        form=signup()
        return render(request,"signup.html",{"form":form})
    def post(self,request):
        form=signup(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            p=form.cleaned_data.get("Name")
            print(p)
        else:
            print("invalid")
        form=signup()

        return render(request,"signup.html",{"form":form})
    
# class Signin(View):
#     def get(self,request):
#         form=signin()
#         return render(request,"signin.html",{"form":form})
#     def post(self,request):
#         form=signin(request.POST)
#         if form.is_valid():
#            name=form.cleaned_data.get("name")
#            email=form.cleaned_data.get("email")
#            password1=form.cleaned_data.get("password")
#            password2=form.cleaned_data.get("Reenter_password")
#            if password1==password2:
#                print(form.cleaned_data)
#                print("match")
        #    else:
        #        print(form.cleaned_data)
        #        print(" not match")
        # else:
        #     print("leave it")
        #     form=signin()

                          
        # return render(request,"signin.html",{"form":form})
    
                            #    OR

class Signin(View):
    def get(self,request):
        form=signin()
        return render(request,"signin.html",{"form":form})
    def post(self,request):
        form=signin(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password')==form.cleaned_data.get('Reenter_password'):
                print(form.cleaned_data)
                
            else:
               print(form.cleaned_data)
               print(" not match")
        else:
            print("leave it")
            form=signin()

        return render(request,"signin.html",{"form":form})

class HelloworldView(View):
    def get(self,request): 
        return render(request,"helloworld.html")
    
class HelloView(View):
    def get(self,request):
        return render(request,"Hello.html")
    
class HloView(View):
    def get(self,request):
        return render(request,"Hlo.html")
    def post(self,request):
        print(request.POST)
        request.POST.get("num1")
        request.POST.get("num2")
        n1=int(request.POST["num1"])
        n2=int(request.POST["num2"])
        result=n1+n2
        print(result)
        return render(request,"Hlo.html",{"result":result})
    
class subView(View):
    def get(self,request):
        return render(request,"sub.html")
    def post(self,request):
        print(request.POST)
        request.POST.get("num1")
        request.POST.get("num2")
        n1=int(request.POST["num1"])
        n2=int(request.POST["num2"])
        result=n1-n2
        print(result)
        return render(request,"sub.html",{"result":result})
class mul(View):
    def get(self,request):
        return render(request,"mul.html")
    def post(self,request):
        print(request.POST)
        request.POST.get("num1")
        request.POST.get("num2")
        n1=int(request.POST["num1"])
        n2=int(request.POST["num2"])
        result=n1*n2
        print(result)
        return render(request,"mul.html",{"result":result})

class divView(View):
    def get(self,request): # serverilekk request kodukkunnu oru data or informationu vendi ,server athinu respond cheyyunnu
        return render(request,"div.html")
    def post(self,request):
        print(request.POST)  # send the data to the server
        request.POST.get("num1") # num1 and num2 keys aahn athine get cheyyan , djangoyil datayellam key value pair aayittanu store cheyyunnath
        request.POST.get("num2")
        n1=int(request.POST["num1"]) # num1 (num1 key aahn) square bracketil aahn so num1 il nammal eth value aahno koduthe athine edukan
        n2=int(request.POST["num2"])
        result=n1/n2
        print(result)
        return render(request,"div.html",{"result":result})
    
class Number(View):
    def get(self,request):
        return render (request,"num.html")
    def post(self,request):
        request.POST.get("number")
        num=int(request.POST.get("number"))
        if num%2==0:
            res='even'
        else:
            res='odd'
        return render(request,"num.html",{"result":res})
    
class Leap(View):
    def get(self,request):
        return render(request,"leap.html")
    def post(self,request):
        request.POST.get("year")
        leap=int(request.POST.get("year"))
        if leap%400==0 and leap%100==0:
            res='leap year'
        elif leap%4==0 and leap%100!=0:
            res='leap year'
        else:
            res='not leap year'
        return render(request,"leap.html",{"result":res})
    
class large(View):
    def get(self,request):
        return render(request,"large.html")
    def post(self,request):
        request.POST.get("num1")
        request.POST.get("num2")
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        if num1>num2:
            res= f"{num1} is large"
        else:
            res= f"{num2} is large"
        return render(request,"large.html",{"result":res})
    
class armstrong(View):
    def get(self,request):
        return render(request,"armstrong.html")
    def post(self,request):
        request.POST.get("num")
        num=int(request.POST.get("num"))
        sum=0
        temp=num
        while(num>0):
            dig=num%10
            sum+=dig**3
            num//=10
            if temp==sum:
                result= "armstrong number"
            else:
                result= "not an armstrong number"
        return render(request,"armstrong.html",{"result":result})
    
class palindrome(View):
    def get(self,request):
        return render(request,"palindrome.html")
    def post(self,request):
        request.POST.get("num")
        num=int(request.POST.get("num"))
        rev=0
        temp=num
        while(num>0):
            dig=num%10
            rev=rev*10+dig
            num//=10
            if rev==temp:
                res="Palindrome"
            else:
                res="Not palindrome"
        return render(request,"palindrome.html",{"result":res})
    
class pali(View):
    def get(self,request):
        return render(request,"pali.html")
    def post(self,request):
        request.POST.get("strng")
        strng=request.POST.get("strng")
        s=strng[::-1]
        if s==strng:
            res= "palindrome"
        else:
            res=" not palindrome"
        return render(request,"pali.html",{"result":res})
    
class dic(View):
    def get(self,request):
        return render(request,"dic.html")
    def post(self,request):
        request.POST.get("str")
        abc=(request.POST["str"])
        s="({})"
        if abc==s:
            res="valid"
        else:
            res="invalid"
        return render(request,"dic.html",{"result":res})

class name(View):
    def get(sel,request):
        return render(request,"name.html")
    def post(self,request):
        request.POST.get("name")
        str=request.POST.get("name")
        res=f" Hello {str} welcome to luminar"
        return render(request,"name.html",{"result":res})
    
class prime(View):
    def get(sel,request):
        return render(request,"prime.html")
    def post(self,request):
        request.POST.get("num")
        num=int(request.POST.get("num"))
        if num==1:
            res=" 1 is not a prime number"
        elif(num==2):
           res=" 2 is a prime number"
        else:
           for i in range(2,num):
                if num%i==0:
                    res="not prime"
                    break
                else:
                    res="prime"
        return render(request,"prime.html",{"result":res}) 

class fibanocci(View):
    def get(self,request):
        return render(request,"fib.html")
    def post(self,request):
        request.POST.get("num",0)
        num=int(request.POST["num"])
        n1=0
        n2=1
        count=0
        res=""
        if num<=0:
            res="The fibannoci series is"
        elif num==1: 
            res=f"{n1}"
        else:
            while count<num:
                res+=f"{n1} "
                n3=n1+n2
                n1=n2
                n2=n3
                count+=1
        return render(request,"fib.html",{"result":res})



            





