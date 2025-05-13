from django.shortcuts import render, redirect
from .forms import AdminLoginForm
from .models import AdminUser
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            try:
                admin = AdminUser.objects.get(username=uname, password=pwd)
                request.session['admin_logged_in'] = True
                return redirect('admin_dashboard')
            except AdminUser.DoesNotExist:
                messages.error(request, 'Invalid username or password')
    else:
        form = AdminLoginForm()
    return render(request, 'adminapp/login.html', {'form': form})

def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    return render(request, 'adminapp/dashboard.html')  # Display admin operations here

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')
