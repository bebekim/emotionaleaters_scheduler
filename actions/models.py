from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Action(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(default=now, editable=False, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.emotion

    def get_absolute_url(self):
        return reverse('action_detail', args=[str(self.id)])