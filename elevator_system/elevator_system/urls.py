from django.urls import include, path
from rest_framework import routers
from elevator.viewsets import ElevatorViewSet, RequestViewSet

router = routers.DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'requests', RequestViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/elevators/<int:pk>/move_up/',
         ElevatorViewSet.as_view({'post': 'move_up'}), name='elevator-move-up'),
    path('api/elevators/<int:pk>/move_down/',
         ElevatorViewSet.as_view({'post': 'move_down'}), name='elevator-move-down'),
    path('api/elevators/<int:pk>/stop/',
         ElevatorViewSet.as_view({'post': 'stop'}), name='elevator-stop'),
    # Add other URL patterns if needed
]
