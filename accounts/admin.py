from django.contrib import admin
from django.contrib.auth.models import User
from .models import User_detail, Ip_adress

class ImageInline(admin.TabularInline):
    model = Ip_adress
    extra = 0



class PersonAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

    
admin.site.register(Ip_adress)
admin.site.register(User_detail, PersonAdmin)



# Register your models here.
