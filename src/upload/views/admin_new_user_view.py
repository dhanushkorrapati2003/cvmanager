# views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from upload.forms import AdminNewUserForm

def admin_add_new_user(request):
    if request.method == 'POST':
        form = AdminNewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create a user object but don't save it yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user object

            return redirect('admin-search')  # Redirect to a profile page or another view
    else:
        form = AdminNewUserForm()
    return render(request, 'admin/admin_new_user.html', {'form': form})
