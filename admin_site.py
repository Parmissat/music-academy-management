# core/admin_site.py
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

class CustomAdminSite(AdminSite):
    site_header = _("مدیریت آموزشگاه موسیقی")
    site_title = _("پنل مدیریت")
    index_title = _("به سیستم مدیریت آموزشگاه خوش آمدید")

custom_admin_site = CustomAdminSite(name='custom_admin')