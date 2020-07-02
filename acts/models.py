from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.

class ActionCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    tags = TaggableManager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass



class Act(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(ActionCategory, on_delete=models.CASCADE, blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

