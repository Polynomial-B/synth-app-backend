from rest_framework import serializers
from ..models import Sequencer

class SequencerSerializer(serializers.ModelSerializer):
	class Meta:
		sequencer = Sequencer
		fields = '__all__'
