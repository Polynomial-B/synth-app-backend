from rest_framework import serializers
from ..models import Sequencer

class SequencerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sequencer
		fields = '__all__'
