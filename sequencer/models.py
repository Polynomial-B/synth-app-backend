from django.contrib.postgres.fields import ArrayField
from django.db import models

class Sequencer(models.Model):
    def __str__(self):
        return f'{self.names}'
    name = models.CharField(max_length=80)
    sequencer = ArrayField(ArrayField(models.IntegerField()))
    

