from django.contrib import admin
from myguest.models import Guest

# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'regdate')  # list_display는 고정
    
admin.site.register(Guest, GuestAdmin)