from django.contrib import admin

from anonymous_blog.models import Message


@admin.register(Message)
class Admin(admin.ModelAdmin):
    pass
