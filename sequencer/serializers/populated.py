from .common import SequencerSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedSequencerSerializer(SequencerSerializer):
	owner = UserSerializer()