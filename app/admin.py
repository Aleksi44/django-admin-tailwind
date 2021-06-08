from django.contrib import admin
from django.contrib.auth.models import Permission, ContentType
from django.contrib.sessions.models import Session

admin.site.register(Session)
admin.site.register(Permission)
admin.site.register(ContentType)
