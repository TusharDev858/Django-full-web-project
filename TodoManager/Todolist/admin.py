from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Register your models here.
from Todolist.models import Task
from Todolist.models import Contact


admin.site.register(Task)
admin.site.register(Contact)

admin.site.site_header = "My Custom Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Admin Dashboard"
