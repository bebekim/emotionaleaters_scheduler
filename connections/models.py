from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Connection(models.Model):
    MEDIA_CHOICES = [
        ('Audio', (
                ('vinyl', 'Vinyl'),
                ('cd', 'CD'),
            )
        ),
        ('Video', (
                ('vhs', 'VHS Tape'),
                ('dvd', 'DVD'),
            )
        ),
        ('unknown', 'Unknown'),
    ]

    emotion = models.CharField(
        max_length=50,
        choices=MEDIA_CHOICES,
        default='unknown'
    )
    reason = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False, blank=True)

    def __str__(self):
        return self.emotion

    def get_absolute_url(self):
        return reverse('connection_detail', args=[str(self.id)])