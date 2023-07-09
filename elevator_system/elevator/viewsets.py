from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['post'])
    def perform_elevator_operation(self, request, pk=None):
        elevator = self.get_object()
        operation = request.data.get('operation')

        if operation == 'move_up':
            # Implement the logic to move the elevator up
            elevator.direction = 'up'
            elevator.save()
            return Response({'message': 'Elevator is moving up.'})

        elif operation == 'move_down':
            # Implement the logic to move the elevator down
            elevator.direction = 'down'
            elevator.save()
            return Response({'message': 'Elevator is moving down.'})

        elif operation == 'stop':
            # Implement the logic to stop the elevator
            elevator.direction = 'stopped'
            elevator.save()
            return Response({'message': 'Elevator has stopped.'})

        else:
            return Response({'error': 'Invalid operation.'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        # Add additional information to the response, such as elevator status
        status_info = {'status': 'Elevator status information'}
        return Response({'elevators': serializer.data, 'status_info': status_info})


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    # Implement additional actions for request operations here
