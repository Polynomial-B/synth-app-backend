from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation #password validation is the function that runs when we create a superuser
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True) # won't appear on UI
	password_confirmation = serializers.CharField(write_only=True)

	def validate(self, data):
		password = data.pop('password')
		password_confirmation = data.pop('password_confirmation')

		if password != password_confirmation:
			raise ValidationError({'password_confirmation': 'passwords do not match'})

		try:
			password_validation.validate_password(password=password)
		except ValidationError as error:
			raise ValidationError({'password': error.messages})

		data['password'] = make_password(password)
		return data
		
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'password_confirmation')