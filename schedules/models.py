import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify

# Create your models here.
class ActionCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    tags = TaggableManager(help_text="tag at your convenience", blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Act(models.Model):
    class Confidence(models.IntegerChoices):
        UP = 1
        NEUTRAL = 0
        DOWN = -1

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(ActionCategory, on_delete=models.CASCADE, blank=True)
    # https://learndjango.com/tutorials/django-slug-tutorial
    slug = models.SlugField(max_length=200, null=False, unique=True, db_index=True)
    description = models.TextField(blank=True)
    tags = TaggableManager(help_text="tag at your convenience", blank=True)
    builds_confidence = models.IntegerField(choices=Confidence.choices)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    # reviewed_at: 
    # next_review_at: 
    # request_review_count


    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('act_detail', args=[str(self.id)])

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)




class Schedule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    # later on, there will be multiple participants for each table
    # thus make this manytomany relationship later
    # for now, this is many to one
    participant = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    scheduled_at = models.DateTimeField()
    acts = models.ManyToManyField(Act, through='ScheduleAct')
    
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
        
