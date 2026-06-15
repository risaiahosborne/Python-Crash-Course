from django.contrib import admin

from .models import Topic, Entry # the (.) is used to make sure it looks within the same directory

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)