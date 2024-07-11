from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
class AuthenticationAdmin():
    def admin_login(request):
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            admin_user = User.objects.filter(username = username)

            if not admin_user.exists():
                messages.info(request, f'{username} Username id not recorded as admin manager ** ') 
                return redirect('admin-login')   
            
            admin_user = authenticate(username=username, password= password)

            if admin_user is not None and admin_user.is_superuser:
                login(request, admin_user)
                messages.success(request, 'login successful')
                return redirect('dashboard')
            messages.info(request, 'Invalid password')
            return redirect('admin-login')    
        return render(request, 'main/login.html')
    @login_required(login_url='admin-login')
    def SignOut(request):
        logout(request)
        return redirect('admin-login')

@login_required(login_url='admin-login')
def dashboard(request):
    return render(request, 'main/dashboard.html')

@login_required(login_url='admin-login')
def myprofile(request):
    return render(request, 'main/myprofile.html')
