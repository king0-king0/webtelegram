from django.contrib import admin
from .models import Media, DataItem,Type_of_home
# Register your models here.
admin.site.register(DataItem)
admin.site.register(Media)
admin.site.register(Type_of_home)