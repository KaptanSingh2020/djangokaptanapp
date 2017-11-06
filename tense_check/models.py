from django.db import models
from django.utils import timezone


class Sentence(models.Model):
    text = models.CharField(max_length=50)
    test_res_pass = models.CharField(max_length=50, default='', blank=True)
    test_res_fail = models.CharField(max_length=50, default='', blank=True)
    TENSE_CHOICES = (
        ('past simple positive', 'past simple positive'),
        ('past simple negative', 'past simple negative'),
        ('past simple yes-no question', 'past simple yes-no question'),
    )
    tense_choice = models.CharField(max_length=50, choices=TENSE_CHOICES, default='past simple positive',
                                    null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
