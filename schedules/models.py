import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


# Create your models here.
class ActionCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    tags = TaggableManager(help_text="tag at your convenience", blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Act(models.Model):

    class Confidence(models.IntegerChoices):
        UP = 1
        NEUTRAL = 0
        DOWN = -1

    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(ActionCategory, on_delete=models.CASCADE, blank=True)
    tags = TaggableManager(help_text="tag at your convenience", blank=True)
    # make this enum: build confident - up/0/down
    builds_confidence = models.IntegerField(choices=Confidence.choices)
    image = models.ImageField(null=True, blank=True)
    # reviewed_at: 
    # next_review_at: 
    # request_review_count

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass



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
        
