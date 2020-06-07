from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.
class Connection(models.Model):
    MEDIA_CHOICES = [
        ('unknown', 'Unknown'),
        ('Happy', (
                ('appreciative', 'Appreciative'),
                ('blissful', 'Blissful'),
                ('confident', 'Confident'),
                ('connected', 'Connected'),
                ('encouraged', 'Encouraged'),
            )
        ),
        ('Afraid', (
                ('anxious', 'Anxious'),
                ('concerned', 'Concerned'),
                ('defensive', 'Defensive'),
                ('distressed', 'Distressed'),
                ('edgy', 'Edgy'),
                ('overwhelmed', 'Overwhelmed'),
                ('powerless', 'Powerless'),
                ('worried', 'Worried'),
            )
        ),
        ('Hurt', (
                ('discarded', 'Discarded'),
                ('insulted', 'Insulted'),
                ('rejected', 'Rejected'),
                ('unwanted', 'Unwanted'),
            )
        ),
        ('Guilty', (
                ('bad', 'Bad'),
                ('regretful', 'Regretful'),
                ('responsible', 'Responsible'),
                ('wrong', 'Wrong'),
            )
        ),
        ('Angry', (
                ('annoyed', 'Annoyed'),
                ('bitter', 'Bitter'),
                ('fed up', 'Fed up'),
                ('grumpy', 'Grumpy'),
                ('irritated', 'Irritated'),
                ('jeaous', 'Jealous'),
                ('upset', 'Upset'),
                ('vengeful', 'Vengeful'),
            )
        ),
        ('Ashamed', (
                ('disgraced', 'Disgraced'),
                ('embarrassed', 'Embarrassed'),
                ('exposed', 'Exposed'),
                ('foolish', 'Foolish'),
                ('humiliated', 'Humiliated'),
                ('mortified', 'Mortified'),
                ('self-conscious', 'Self-conscious'),
                ('unworthy', 'Unworthy'),
                ('vulnerable', 'Vulnerable'),
            )
        ),
        ('Sad', (
                ('blue', 'Blue'),
                ('depressed', 'Depressed'),
                ('disappointed', 'Disappointed'),
                ('down', 'Down'),
                ('empty', 'Empty'),
                ('miserable', 'Miserable'),
                ('irritable', 'Irritable'),
                ('unwanted', 'Unwanted'),
                ('withdrawn', 'Withdrawn'),
            )
        ),
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