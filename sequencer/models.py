from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import JSONField

class Sequencer(models.Model):
    def __str__(self):
        return f'{self.name} - {self.owner}'
    name = models.CharField(max_length=80)
    sequencer = ArrayField(
        models.JSONField(default=dict),
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name="sequencer",
        on_delete=models.CASCADE
    )
