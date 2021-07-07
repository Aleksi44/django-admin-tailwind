from django.db import models


class TagModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class DataModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    long_long_long_long_long_char_field = models.CharField(max_length=200, default=None, null=True, blank=True)
    text_field = models.TextField(default=None, null=True, blank=True)
    number_field = models.IntegerField(default=None, null=True, blank=True)
    url_field = models.URLField(max_length=500, default=None, null=True)
    tag = models.ForeignKey(TagModel, on_delete=models.SET_NULL, null=True)
