from django.contrib import admin
from .models import admin_info,student,company,login_info,feedback
# Register your models here.
class adminInfo(admin.ModelAdmin):
    list_display=['email']
class studentInfo(admin.ModelAdmin):
    list_display=['email']
class companyInfo(admin.ModelAdmin):
    list_display=['name']
class loginInfo(admin.ModelAdmin):
    list_display=['username']
class feedbackInfo(admin.ModelAdmin):
    list_display=["email"]
admin.site.register(admin_info,adminInfo)
admin.site.register(company,companyInfo)
admin.site.register(student,studentInfo)
admin.site.register(login_info,loginInfo)
admin.site.register(feedback,feedbackInfo)