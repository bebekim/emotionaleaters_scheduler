from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.timezone import now
from connections import models as connection_models
import datetime

# Create your models here.
class Vice(models.Model):

    class ConsumptionArea(models.TextChoices):
        SAFESPACE = 'SAFESPACE', _('Safe Space')
        COMMONAREA = 'COMMONAREA', _('Common Area')
        KITCHEN = 'KITCHEN', _('Kitchen')
        MOVING = 'MOVING', _('Moving')
        RESTAURANT = 'RESTAURANT', _('Restaurant')
        
    location = models.CharField(
        max_length=50,
        choices=ConsumptionArea.choices,
        default=ConsumptionArea.SAFESPACE
    )

    TIME_CHOICES = [
        ('unspecified', 'Unspecified'),
        ('Early morning', (
                ('planning', 'Planning'),
                ('working', 'Working'),
            )
        ),
        ('Breakfast', (
                ('before meal prep', 'Before Meal Prep'),
                ('during meal', 'During Meal'),
                ('after meal prep', 'After Meal Prep'),
            )
        ),
        ('Kids at School', (
                ('on commute', 'On Commute'),
                ('return home', 'Return Home'),
            )
        ),
        ('At work', (
                ('plan for day', 'Plan for Day'),
                ('before meeting', 'Before Meeting'),
                ('during meeting', 'During Meeting'),
                ('after meeting', 'After Meeting'),
                ('roadblocked', 'Roadblocked'),
                ('hard at work', 'Hard at Work'),
                ('break', 'Break'),
                ('interrupted', 'Interrupted'),
            )
        ),
        ('Kids at Home', (
                ('house chore', 'House Chore'),
                ('finish work', 'Finish Work'),
                ('spend time with children', 'Spend Time with Children'),
            )
        ),
        ('Kids asleep', (
                ('finish up house chore', 'Finish up House Chore'),
                ('time with partner', 'Time with Partner'),
                ('alone time', 'Alone Time'),
            )
        ),
    ]

    occasion = models.CharField(
        max_length=50,
        choices=TIME_CHOICES,
        default='unspecified'
    )

    connection = models.ForeignKey(
        connection_models.Connection,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class StressSource(models.TextChoices):
        SELF = 'SELF', _('Self')
        PARTNER = 'PARTNER', _('Partner')
        CHILD = 'CHILD', _('Child')
        PARENT = 'PARENT', _('Parent')
        SIBLING = 'SIBLING', _('Sibling')
        FRIEND = 'FRIEND', _('Friend')
        EMPLOYER = 'EMPLOYER', _('Employer')
        SUPERVISOR = 'SUPERVISOR', _('Supervisor')
        EMPLOYEE = 'EMPLOYEE', _('Employee')
        COLLEAGUE = 'COLLEAGUE', _('Colleague')
        RANDOM = 'RANDOM', _('Random')

    involved_one = models.CharField(
        max_length=50,
        choices=StressSource.choices,
        default=StressSource.SELF,
        null=True,
        blank=True
    )

    consumption = models.CharField(max_length=50)
    consumption_date = models.DateField(_("Date"), default=datetime.date.today)
    
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    created_date = models.DateTimeField(default=now, editable=False, blank=True)


    def __str__(self):
        return self.consumption

    # def get_absolute_url(self):
    #     return reverse('vice_detail', args=[str(self.id)])