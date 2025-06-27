from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import JobseekerRegistrationForm, EmployerRegistrationForm, LoginForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout, get_user_model
User = get_user_model()


def jobseeker_register(request):
    # POST to handle form submissiom
    if request.method == 'POST':
        form = JobseekerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        # If form invalid, this show errors with submitted data
        return render(request, 'accounts/jobseeker_register.html', {'seekerform': form})
    
    # for GET bring blank form
    form = JobseekerRegistrationForm()
    return render(request, 'accounts/jobseeker_register.html', {'seekerform': form})
    

def employer_register(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'accounts/employer_register.html', {'employerform': form})
    form = EmployerRegistrationForm()  
    return render(request, 'accounts/employer_register.html', {'employerform': form})

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if hasattr(user, 'role') and user.role =='jobseeker':
                    return redirect('jobseeker_dashboard')
                elif hasattr(user, 'role') and user.role =='employer':
                    return redirect('employer_dashboard')
    context = {
        'loginform': form
                }
    return render(request, 'accounts/login.html',context=context)

def jobseeker_dashboard(request):
    template = loader.get_template('accounts/jobseeker_dashboard.html')
    return HttpResponse(template.render())

def employer_dashboard(request):
    template = loader.get_template('accounts/employer_dashboard.html')
    return HttpResponse(template.render())
    
            
            
