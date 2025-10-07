from django.contrib import admin
from django.urls import path
from core.views import monthly_report, dashboard  , quick_attendance 
from core.views import home 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    path('', home, name='home'),  
    path('admin/quick-attendance/', quick_attendance, name='quick_attendance'),
    path('report/', monthly_report, name='monthly_report'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/', admin.site.urls)
    
]
 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)