import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Conditioning(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    theme = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=now, editable=False, blank=True)
    updated_date = models.DateTimeField(auto_now=True, editable=True, blank=True)

    def __str__(self):
        return self.theme

    # def get_absolute_url(self):
    #     return reverse('conditioning_detail', args=[str(self.id)])