from django.contrib.postgres.fields import ArrayField
from django.db import models

class Sequencer(models.Model):
    def __str__(self):
        return f'{self.sequencer}'
    sequencer = ArrayField(ArrayField(models.IntegerField()))
    

