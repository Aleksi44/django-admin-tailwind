from django.contrib import admin
from django.contrib.auth.models import Permission, ContentType
from django.contrib.sessions.models import Session
from app.models import TagModel, DataModel


class DataAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'long_long_long_long_long_char_field',
        'text_field',
        'number_field',
        'url_field'
    )
    readonly_fields = ('created',)
    list_filter = (
        ('tag', admin.RelatedOnlyFieldListFilter),
    )
    search_fields = ('number_field',)


admin.site.register(Session)
admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(DataModel, DataAdmin)
admin.site.register(TagModel)
