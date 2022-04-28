from django.contrib import admin

from .models import User, create_listing

# Register your models here.
class create_listingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image", "Category")

admin.site.register(User)
admin.site.register(create_listing)

