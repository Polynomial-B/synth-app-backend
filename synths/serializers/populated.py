from .common import SynthSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedSynthSerializer(SynthSerializer):
	owner = UserSerializer()