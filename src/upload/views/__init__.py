from .upload_view import *
from .search_view import *
from .login_view import *
from .admin_login_view import *
from .admin_search_view import *
from .admin_new_user_view import *
from .admin_history_view import *
from .admin_upload_view import *
from .admin_resume_report import *
from .detail_view import * 
from .admin_detail_view import *

#Only error pages defined here
def custom_404_view(request):
    return render(request, '404.html')