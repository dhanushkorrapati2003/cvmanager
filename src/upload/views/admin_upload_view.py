from django.shortcuts import render, redirect,  get_object_or_404
from upload.forms import PersonForm
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from upload.forms import PersonForm
from upload.models import Person, AuditLog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def admin_upload(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                person = form.save(commit=False)  # Create the Person instance without saving it yet
                person.author = request.user  # Set the author to the currently logged-in user
                person.save()

                # Create an audit log entry for the addition
                person_id = person.id
                before = " "
                after = f"{person.first_name} {person.last_name} {person.phone_number} {person.email} {person.resume}"
                AuditLog.objects.create(person_id=person_id, username=request.user, action="create", before=before, after=after)

                return redirect('admin-success')
            except IntegrityError as e:
                messages.error(request, 'An error occurred. Please check your data.')
    else:
        form = PersonForm()

    return render(request, 'admin/admin_upload.html', {'form': form}) 

@login_required
def admin_success(request):
    return render(request, 'admin/admin_success.html')

@login_required

def admin_edit_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            new_resume = request.FILES.get('new_resume')  # Use 'new_resume' field
            before = f"{person.first_name} {person.last_name} {person.phone_number} {person.email} {person.resume}" # Create an audit log entry before updating the person
            if new_resume:
                person.resume = new_resume
                person.save()

            updated_person = form.save()
            after = f"{updated_person.first_name} {updated_person.last_name} {updated_person.phone_number} {updated_person.email} {updated_person.resume}" # Create an audit log entry after updating the person
            person_id = person.id
            AuditLog.objects.create(person_id=person_id, username=request.user, action="update", before=before, after=after)

            return redirect('admin-search')
    else:
        form = PersonForm(instance=person)

    return render(request, 'admin/admin_edit_person.html', {'form': form, 'person': person})



@login_required
def admin_delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    if request.method == 'POST':
        # Create an audit log entry before deleting the person
        person_id = person.id
        before = f"{person.first_name} {person.last_name} {person.phone_number} {person.email} {person.resume}"
        after = " "
        AuditLog.objects.create(person_id=person_id, username=request.user, action="delete", before=before, after=after)

        person.delete()
        return redirect('admin-search')

    return render(request, 'admin/admin_delete_person.html', {'person': person})

@csrf_exempt
@login_required
def delete_selected(request):
    if request.method == "POST":
        selected_items = request.POST.getlist("selected_items[]")
        for person_id in selected_items:
            person = get_object_or_404(Person, id=person_id)
            before = f"{person.first_name} {person.last_name} {person.phone_number} {person.email}"
            after = " "
            AuditLog.objects.create(person_id=person_id, username=request.user, action="delete", before=before, after=after)

            person.delete()
            
        return JsonResponse({"message": "Selected items deleted successfully."})
        

    return JsonResponse({"message": "Invalid request method."}, status=400)