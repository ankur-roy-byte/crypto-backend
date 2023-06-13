from django.contrib import admin

from .models import SmsStats ,Profile,MyCoin,User
from django.contrib.auth import get_user_model  # If used custom user model
from django.contrib.auth.admin import UserAdmin

# UserModel = get_user_model()
#
# admin.site.register(UserModel)
admin.site.register(User, UserAdmin)

class MyCoinAdmin(admin.ModelAdmin):
    # raw_id_fields = ("coinCode",)
    search_fields = ['MyCoin__coinCode']
    list_display = ('coinCode', 'halfHourPercentage','alarmPercentage','goodNewsPercentage','myprice')


admin.site.register(MyCoin,MyCoinAdmin)
admin.site.register(SmsStats)
admin.site.register(Profile)