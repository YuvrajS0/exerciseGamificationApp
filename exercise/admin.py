from django.contrib import admin
from .models import Workout
from embed_video.admin import AdminVideoMixin
from .models import Item
# Register your models here.

admin.site.register(Workout)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
