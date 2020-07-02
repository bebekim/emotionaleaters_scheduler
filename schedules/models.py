import uuid
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from acts.models import Act

# Create your models here.
class Schedule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    transaction_id = models.CharField(max_length=200, null=True)
    participant = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    scheduled_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.id}"



class ScheduleAct(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    act = models.ForeignKey(
        Act,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.created_at}"
        
