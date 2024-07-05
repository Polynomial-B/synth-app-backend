from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from datetime import datetime, timedelta # timestamps in diff formats
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializers import UserSerializer


User = get_user_model()


class RegisterView(APIView):

	def post(self, request):
		user_to_create = UserSerializer(data=request.data)

		if user_to_create.is_valid():
			user_to_create.save()
			return Response({'message': 'User Created Successfully'}, status=status.HTTP_201_CREATED)
		return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
	

class LoginView(APIView):
	
    def post(self, request):
        
        username = request.data.get('username')
        password = request.data.get('password')
		
        try:
            user_to_login = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied(detail="Invalid Credentials")
        
        if not user_to_login.check_password(password):
            raise PermissionDenied(detail="Invalid Credentials")
        
        #? timedelta = token length (like JS Date()
        # We combine to make a time/data expiry of the issued token
        dt = datetime.now() + timedelta(days=7)

        token = jwt.encode(
            {'sub': user_to_login.id, 'exp': int(dt.strftime('%s'))},
            settings.SECRET_KEY, 
            algorithm='HS256'
        )

        return Response({'token': token, 'message': f"Welcome back, {user_to_login.username}"})