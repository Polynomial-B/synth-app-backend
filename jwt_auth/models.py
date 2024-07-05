from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
	email = models.CharField(max_length=50, unique=True, validators=[
		RegexValidator(
                # validator regex for email
                regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
                message="Enter a valid email",
                code="invalid_registration",
            ),
	],)
