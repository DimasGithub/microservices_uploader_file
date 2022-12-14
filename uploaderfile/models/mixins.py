from django.db import models

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    deleted_at = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    class Meta:
        abstract = True