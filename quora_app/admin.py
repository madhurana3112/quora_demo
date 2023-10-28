from django.contrib import admin
from quora_app.models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)