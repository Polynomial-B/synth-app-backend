from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

class Synth(models.Model):
    def __str__(self):
        return f'{self.name}'
    
    name = models.CharField(max_length=80)
    a_d_s_r = ArrayField(models.IntegerField())
    waveform = models.CharField(max_length=20)
    effects = ArrayField(
            models.JSONField(default=dict),
            blank=True,
            null=True
    )

    freqs = ArrayField(models.IntegerField())
    
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name="synth",
        on_delete=models.CASCADE
    )

