from django.contrib import admin
from first_app.models import AccessRecord, Topic, UserProfileInfo, Webpage

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
