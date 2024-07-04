from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Sequencer
from .serializers.common import SequencerSerializer
from .serializers.populated import PopulatedSequencerSerializer

class SequencerListView(APIView):
	permission_classes = (IsAuthenticatedOrReadOnly, )
	
	def get(self, _request):
		sequencers = Sequencer.objects.all()
		serialized_sequencers = SequencerSerializer(sequencers, many=True)
		return Response(serialized_sequencers.data, status=status.HTTP_200_OK)
	
	def post(self, request):
		request.data["owner"] = request.user.id

		sequencer_to_add = SequencerSerializer(data=request.data)
		
		try:
			sequencer_to_add.is_valid()
			sequencer_to_add.save()
			return Response(sequencer_to_add.data, status=status.HTTP_201_CREATED)
		
		except Exception as e:
			print("Error")
			return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class SequencerDetailView(APIView):
	permission_classes = (IsAuthenticatedOrReadOnly, )
	def get_sequencer(self, pk):
		try:
			return Sequencer.objects.get(pk=pk)
		except Sequencer.DoesNotExist:
			raise NotFound(detail="Can't get sequencer")

	def get(self, _request, pk):
		sequencer = self.get_sequencer(pk=pk)
		serialized_sequencer = PopulatedSequencerSerializer(sequencer)
		return Response(serialized_sequencer.data, status=status.HTTP_200_OK)

	def put(self, request, pk):

		sequencer_to_edit = self.get_sequencer(pk=pk)
		request.data["owner"] = request.user.id

		if sequencer_to_edit.owner.id != request.user.id and not (request.user.is_staff or request.user.is_superuser):
			return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


		request.data['owner'] = original_owner
		
		original_owner = sequencer_to_edit.owner.id

		updated_sequencer = SequencerSerializer(sequencer_to_edit, data=request.data)
		
		if updated_sequencer.is_valid():
			updated_sequencer.save()
			return Response(updated_sequencer.data, status=status.HTTP_202_ACCEPTED)
		
		return Response(updated_sequencer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
		

	def delete(self, request, pk):
		sequencer_to_delete = self.get_sequencer(pk=pk)

		if sequencer_to_delete.owner != request.user and not (request.user.is_staff or request.user.is_superuser):

			return Response(status=status.HTTP_401_UNAUTHORIZED)

		sequencer_to_delete.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

