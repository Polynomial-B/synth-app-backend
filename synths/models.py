from django.db import models
from django.contrib.postgres.fields import ArrayField

class Synth(models.Model):
    def __str__(self):
        return f'{self.name}'
    
    name = models.CharField(max_length=80)
    a_d_s_r = ArrayField(models.IntegerField())
    freqs = ArrayField(models.IntegerField())
    
    owner = models.ForeignKey(
    'jwt_auth.User',
    related_name="synths",
    on_delete=models.CASCADE
)