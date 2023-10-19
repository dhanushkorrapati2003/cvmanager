from django.shortcuts import render
from upload.models import Person, CustomUser
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

def admin_resume_report(request):
    # Fetch all CustomUser objects
    users = CustomUser.objects.all()

    # Create a dictionary to store user details and resumes
    resumes_by_user = {}
    
    for user in users:
        # Fetch all Person objects with this user as the author
        resumes = Person.objects.filter(author=user)
        
        # If there are resumes associated with this user, add them to the dictionary
        if resumes:
            resumes_by_user[user] = resumes

    return render(request, 'admin/admin_resume_report.html', {'users' : users, 'user_details_and_resumes': resumes_by_user})




def fetch_resumes(request):
    user_id = request.GET.get('user_id')
    user = get_object_or_404(CustomUser, pk=user_id)

    # Fetch all resumes associated with the selected user
    resumes = Person.objects.filter(author=user)
    

    context = {'resumes' : resumes, 'user': user}
    return render(request, 'admin/admin_resumes_table.html', context)
