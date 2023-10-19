from django.urls import path, re_path
import upload.views as views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

urlpatterns = [
    # ...
    path('', RedirectView.as_view(url='/login/'), name='redirect-to-login'),
    
    path('login/', views.custom_login, name='login'),
    path('login', views.custom_login, name='login'),
    
    path('logout/', views.custom_logout, name='logout'),
    path('logout', views.custom_logout, name='logout'),
        
    path('admin/', RedirectView.as_view(url='login/'), name='redirect-to-admin-login'),         # These gymnastiics are based on observations of the behavior of the router
    path('admin', RedirectView.as_view(url='admin/login/'), name='redirect-to-admin-login'),
    
    path('upload/', views.upload, name='upload'),
    path('upload', views.upload, name='upload'),
    
    path('success/', views.success, name='success'),
    path('success', views.success, name='success'),
    
    path('search/', views.search, name='search'),
    path('search', views.search, name='search'),
    
    path('detail/<int:person_id>/', views.detail_person, name='detail-person'),
    
    
    path('edit/<int:person_id>/', views.edit_person, name='edit_person'),
    
    path('delete/<int:person_id>/', views.delete_person, name='delete_person'),
    
    path('admin/login/', views.admin_login, name='admin-login'),
    path('admin/login', views.admin_login, name='admin-login'),
    
    path('admin/logout/', views.admin_logout, name='admin-logout'),
    path('admin/logout', views.admin_logout, name='admin-logout'),
    
    path('admin/search/', views.admin_search, name='admin-search'),
    path('admin/search', views.admin_search, name='admin-search'),
    
    path('admin/upload/', views.admin_upload, name='admin-upload'),
    path('admin/upload', views.admin_upload, name='admin-upload'),
    
    path('admin/success/', views.admin_success, name='admin-success'),
    path('admin/success', views.admin_success, name='admin-success'),
    
    path('admin/add/', views.admin_add_new_user, name='admin-add-new-user'),
    path('admin/add', views.admin_add_new_user, name='admin-add-new-user'),
    
    path('admin/detail/<int:person_id>/', views.admin_detail_person, name='admin-detail-person'),
    
    path('fetch_resumes', views.fetch_resumes, name='fetch-resumes'),
    
    #path('admin/users/', views.admin_users, name='admin-user'),
    #path('admin/users', views.admin_users, name='admin-user'),
    
    path('admin/edit/<int:person_id>/', views.admin_edit_person, name='admin-edit-person'),
    
    path('admin/deleteselected/', views.delete_selected, name='delete-selected'),
    
    path('admin/delete/<int:person_id>/', views.admin_delete_person, name='admin-delete-person'),
    
    path('admin/person/<int:person_id>/history/', views.admin_view_history, name='admin-view-history'),
    path('admin/person/<int:person_id>/history', views.admin_view_history, name='admin-view-history'),
    
    path('admin/resume/report/', views.admin_resume_report, name='admin-resume-report'),
    
    re_path(r'^.*/$', views.custom_404_view)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)