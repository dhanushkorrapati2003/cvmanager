from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('search')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Extract username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Manually authenticate the user without logging them in
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                # User credentials are valid
                login(request, user)  # Log the user in
                return redirect('search')
            else:
                # User credentials are not valid
                form.add_error(None, 'Invalid username or password.')
            
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

