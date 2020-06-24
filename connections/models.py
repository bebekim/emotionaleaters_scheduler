from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Connection(models.Model):
    EMOTION_CHOICES = [
        ('unknown', 'Unknown'),
        ('Afraid', (
                ('anxious', 'Anxious'),
                ('concerned', 'Concerned'),
                ('defensive', 'Defensive'),
                ('overwhelmed', 'Overwhelmed'),
            )
        ),
        ('Angry', (
                ('annoyed', 'Annoyed'),
                ('bitter', 'Bitter'),
                ('fed up', 'Fed up'),
                ('jealous', 'Jealous'),
                ('unappreciated', 'Unappreciated'),
                ('upset', 'Upset'),
                ('vengeful', 'Vengeful'),
            )
        ),
        ('Ashamed', (
                ('disgraced', 'Disgraced'),
                ('exposed', 'Exposed'),
                ('foolish', 'Foolish'),
                ('humiliated', 'Humiliated'),
                ('self-conscious', 'Self-conscious'),
                ('unworthy', 'Unworthy'),
                ('vulnerable', 'Vulnerable'),
            )
        ),
        ('Guilty', (
                ('bad', 'Bad'),
                ('regretful', 'Regretful'),
                ('responsible', 'Responsible'),
                ('wrong', 'Wrong'),
            )
        ),
        ('Hurt', (
                ('discarded', 'Discarded'),
                ('insulted', 'Insulted'),
                ('rejected', 'Rejected'),
                ('unwanted', 'Unwanted'),
            )
        ),
        ('Out of Option', (
                ('directionless', 'Directionless'),
                ('lack of control', 'Lack of Control'),
                ('lost', 'Lost'),
                ('trapped', 'Trapped'),
                ('uncoordinated', 'Uncoordinated'),
            )
        ),
        ('Sad', (
                ('disappointed', 'Disappointed'),
                ('empty', 'Empty'),
                ('miserable', 'Miserable'),
                ('trapped', 'Trapped'),
                ('unwanted', 'Unwanted'),
                ('withdrawn', 'Withdrawn'),
            )
        ),
        ('Worthy', (
                ('deserving', 'Deserving'),
                ('hard working', 'Hard working'),
                ('small win', 'Small win'),
                ('proud', 'Proud'),
            )
        ),
    ]
    id = models.AutoField(primary_key=True)
    emotion = models.CharField(
        max_length=50,
        choices=EMOTION_CHOICES,
        default='unknown'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    reason = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False, blank=True)

    def __str__(self):
        return self.emotion

    def get_absolute_url(self):
        return reverse('connection_detail', args=[str(self.id)])