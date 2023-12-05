"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import HelloworldView,HelloView,HloView,subView,mul,divView,Number,Leap,large,armstrong,palindrome,pali,dic,name,prime,fibanocci,FormView
from operation.views import newview,Emiview,Signup,Signin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',HelloworldView.as_view()),
    path('hlo/',HelloView.as_view()),
    path('Hllo/',HloView.as_view()),
    path('sub/',subView.as_view()),
    path('mul/',mul.as_view()),
    path('div/',divView.as_view()),
    path('number/',Number.as_view()),
    path('year/',Leap.as_view()),
    path('large/',large.as_view()),
    path('arms/',armstrong.as_view()),
    path('pali/',palindrome.as_view()),
    path('palii/',pali.as_view()),
    path('dic/',dic.as_view()),
    path('name/',name.as_view()),
    path('prime/',prime.as_view()),
    path('fib/',fibanocci.as_view()),
    path('form/',FormView.as_view()),
    path('forms/',newview.as_view()),
    path('emi/',Emiview.as_view()),
    path('sign/',Signup.as_view()),
    path('signin/',Signin.as_view())

]

