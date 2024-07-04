from rest_framework import serializers
from ..models import Synth

class SynthSerializer(serializers.ModelSerializer):
	class Meta:
		model = Synth
		fields = '__all__'
