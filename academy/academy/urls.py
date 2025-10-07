from django.contrib import admin
from django.urls import path
from core.views import monthly_report  # این خط باید وجود داشته باشد

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/', monthly_report, name='monthly_report'),  # این خط باید وجود داشته باشد
]