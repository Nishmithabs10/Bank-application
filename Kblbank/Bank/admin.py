from django.contrib import admin

# Register your models here.
from Bank.models import Accountuser, Records, Feedback
admin.site.site_header = 'Bank of Kblbank'
# Register your models here.

admin.site.register(Accountuser)
admin.site.register(Records)
admin.site.register(Feedback)
