
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Synth
from .serializers.common import SynthSerializer
from .serializers.populated import PopulatedSynthSerializer

class SynthListView(APIView):
	permission_classes = (IsAuthenticatedOrReadOnly, )
	
	def get(self, request):
		synths = Synth.objects.filter(owner=request.user.id)
		serialized_synths = SynthSerializer(synths, many=True)
		return Response(serialized_synths.data, status=status.HTTP_200_OK)
	
	def post(self, request):
		request.data["owner"] = request.user.id

		synth_to_add = SynthSerializer(data=request.data)
		
		try:
			synth_to_add.is_valid()
			synth_to_add.save()
			return Response(synth_to_add.data, status=status.HTTP_201_CREATED)
		
		except Exception as e:
			print("Error")
			return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class SynthDetailView(APIView):
	permission_classes = (IsAuthenticatedOrReadOnly, )
	def get_synth(self, pk):
		try:
			return Synth.objects.get(pk=pk)
		except Synth.DoesNotExist:
			raise NotFound(detail="Can't get synth")

	def get(self, _request, pk):
		synth = self.get_synth(pk=pk)
		serialized_synth = PopulatedSynthSerializer(synth)
		return Response(serialized_synth.data, status=status.HTTP_200_OK)

	def put(self, request, pk):

		synth_to_edit = self.get_synth(pk=pk)
		request.data["owner"] = request.user.id

		if synth_to_edit.owner.id != request.user.id and not (request.user.is_staff or request.user.is_superuser):
			return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


		updated_synth = SynthSerializer(synth_to_edit, data=request.data)
		
		if updated_synth.is_valid():
			updated_synth.save()
			return Response(updated_synth.data, status=status.HTTP_202_ACCEPTED)
		
		return Response(updated_synth.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
		

	def delete(self, request, pk):
		synth_to_delete = self.get_synth(pk=pk)

		if synth_to_delete.owner != request.user and not (request.user.is_staff or request.user.is_superuser):

			return Response(status=status.HTTP_401_UNAUTHORIZED)

		synth_to_delete.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

