from django.shortcuts import render,redirect
from django.views import View
from user.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

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
            form_instance.save()
            return redirect('user:userlogin')
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

