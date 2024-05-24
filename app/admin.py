from django.contrib import admin

# Register your models here.
from app.models import *

#registering our tables to admin
admin.site.register(Topic)  

admin.site.register(WebPage)

admin.site.register(AccessRecord)
