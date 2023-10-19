# views.py
from django.shortcuts import render, get_object_or_404
from upload.models import Person

def detail_person(request, person_id):
    # Retrieve the person using the person_id
    person = get_object_or_404(Person, id=person_id)

    # Render the detail view template with the person details
    return render(request, 'detail_person.html', {'person': person})
