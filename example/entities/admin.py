from django.contrib import admin

from entities.models import User, Group

# Register your models here.
admin.site.register(User)
admin.site.register(Group)
