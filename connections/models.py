from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Connection(models.Model):

    class CoreEmotion(models.TextChoices):
        AFRAID = 'AFR', _('Afraid')
        ANGRY = 'ANG', _('Angry')
        ASHAMED = 'SHM', _('Ashamed')
        HAPPY = 'HPY', _('Happy')
        HURT = 'HRT', _('Hurt')
        GUILTY = 'GTY', _('Guilty')
        SAD = 'SAD', _('Sad')

    core_emotion = models.CharField(
        max_length=3,
        choices=CoreEmotion.choices,
        default=CoreEmotion.AFRAID
    )
    reason = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False, blank=True)

    def __str__(self):
        return self.core_emotion

    def get_absolute_url(self):
        return reverse('connection_detail', args=[str(self.id)])