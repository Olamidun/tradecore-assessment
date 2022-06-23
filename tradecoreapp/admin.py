from .models import Post
from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class ListPostAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListPostAdminMixin, self).__init__(model, admin_site)

models = apps.get_models()

for model in models:
    admin_class = type("AdminClass", (ListPostAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
