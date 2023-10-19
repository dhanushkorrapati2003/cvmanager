from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.shortcuts import redirect

def superuser_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            # The user is authenticated and is a superuser
            return view_func(request, *args, **kwargs)
        else:
            # Redirect or deny access for non-superusers
            return redirect('admin-login')  # Redirect to admin login

    return _wrapped_view

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin-search')  # Redirect superusers to the admin search site

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Extract username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Manually authenticate the user without logging them in
            user = authenticate(request=request, username=username, password=password)

            if user is not None and user.is_superuser:
                # User credentials are valid and user is a superuser
                login(request, user)  # Log the superuser in
                return redirect('admin-search')  # Redirect to the admin search site
            else:
                # User credentials are not valid or user is not a superuser
                form.add_error(None, 'Invalid username or password or you are not a superuser.')

    else:
        form = AuthenticationForm()

    return render(request, 'admin/admin_login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('admin-login')
