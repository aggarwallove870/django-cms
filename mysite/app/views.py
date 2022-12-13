from django.shortcuts import HttpResponseRedirect,render,redirect
# Create your views here.
from app.models import *
from django.conf import settings
# from django.core.mail import EmailMessage
from django.core.mail import send_mail
def registerform(request):
    
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        print(first_name)
        last_name = request.POST.get('last_name')
        print(last_name)
        email=  request.POST.get('email_address')
        print(email,"-------HERE")
        name_of_school= request.POST.get('name_of_urschool')
        print(name_of_school)
        grade_level = request.POST.get('grade_level')
        state_province = request.POST.get('state_province')
        flexRadioDefault= request.POST.get('flexRadioDefault')
        obj = RegisterForm(first_name=first_name, last_name=last_name, email_address=email,name_of_school=name_of_school,grade_level=grade_level,state=state_province, flexRadioDefault=flexRadioDefault)
        obj.save()
        subject ="Thankyou for Register"
        message = "You are successfully registered"
        print("--------")
        from_email = settings.EMAIL_HOST_USER
        
        send_mail(subject, message, "loveaggarwal@snakescript.com", [email],fail_silently=True)

        print(from_email,"------++++_____")

        return redirect('http://68.183.194.137/student/')
