from django.contrib import admin
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('id','name','mobno','email','msg')
# Register your models here.
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')
admin.site.register(category,categoryAdmin)

class newsAdmin(admin.ModelAdmin):
    list_display = ('id','ncity','nhead','ncategory','nsubject','ndes','ndate','npic')
admin.site.register(news,newsAdmin)

class videonewsAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vtitle','vnews','vcategory','vcity','vdate')
admin.site.register(videonews,videonewsAdmin)

class notificationAdmin(admin.ModelAdmin):
    list_display = ('id','ndes','ndate')
admin.site.register(notification,notificationAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','spic','stitle','sdate')
admin.site.register(slider,sliderAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','city','cdate')
admin.site.register(city,cityAdmin)
