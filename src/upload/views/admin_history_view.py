from django.shortcuts import render
from upload.models import AuditLog

def admin_view_history(request, person_id):
    # Fetch the AuditLog entries related to the specified person_id
    change_history = AuditLog.objects.filter(person_id=person_id).order_by('-timestamp')

    # Render a template to display the change history
    return render(request, 'admin/admin_history.html', {'change_history': change_history})
