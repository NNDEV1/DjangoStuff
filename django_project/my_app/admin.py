from django.contrib import admin
from my_first_app.models import AcessRecord, Topic, Webpage
# Register your models here.
admin.site.register(AcessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
