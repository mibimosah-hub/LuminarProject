from django.shortcuts import render,redirect
from django.views import View
from user.forms import LoginForm,OTPForm,CustomUser
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home.html')
from user.forms import SignUpForm
class Register(View):
    def get(self, request):
        form_instance=SignUpForm()
        context = {'form':form_instance}
        return render(request, 'register.html',context)

    def post(self, request):
        form_instance=SignUpForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False) #is_active value change to zero before verfication
            u.is_active=False
            u.save()
            u.generate_otp() #creating otp
            send_mail(
                "Django Auth OTP",
                f"Your OTP is: {u.otp}",
                "mibimosah@gmail.com",
                [u.email],
                fail_silently=False,
            ) #send mail to user for getting OTP
            return redirect('user:OTP_Verification')
        else:
            context = {'form':form_instance}
            return render(request, 'register.html',context)

class UserLogin(View):
    def get(self, request):
        from_instance=LoginForm()
        context = {'form':from_instance}
        return render(request, 'login.html',context)

    def post(self, request):
        from_instance=LoginForm(request.POST)
        if from_instance.is_valid():
           username = from_instance.cleaned_data['username']
           password = from_instance.cleaned_data['password']
           user=authenticate(request,username=username,password=password)
           if user and user.is_superuser==True:
                login(request,user)
                return redirect('user:adminhome')
           elif user and user.role=='student':
               login(request,user)
               return redirect('user:studenthome')
           elif user and user.role=='teacher':
               login(request,user)
               return redirect('user:teacherhome')

           else:
                context = {'form':from_instance}
                return render(request, 'login.html',context)

class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('user:userlogin')

class AdminHome(View):
    def get(self, request):
        form_instance=SignUpForm()
        context = {'form':form_instance}
        return render(request, 'adminhome.html')

class StudentHome(View):
    def get(self, request):
        from_instance=SignUpForm()
        context = {'form':from_instance}
        return render(request, 'studenthome.html',context)

class TeacherHome(View):
    def get(self, request):
        from_instance=SignUpForm()
        context = {'form':from_instance}
        return render(request, 'teacherhome.html',context)


class OTP_Verification(View):
    def post(self, request):
        o=request.POST['o']
        try:
            u=CustomUser.objects.get(opt=o)
            u.is_verfied=True
            u.is_active=True
            u.otp=None
            u.save()
            return redirect('user:userlogin')
        except:
            messages.error(request, 'Invaild OTP')
            return redirect('user:OTP_Verification')

    def get(self, request):
        form_instance=OTPForm()
        context = {'form':form_instance}
        return render(request, 'otp_verification.html',context)