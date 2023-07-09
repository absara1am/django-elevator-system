from django.db import models


class Elevator(models.Model):
    STATUS_CHOICES = (
        ('idle', 'Idle'),
        ('running', 'Running'),
        ('maintenance', 'Maintenance'),
    )
    DIRECTION_CHOICES = (
        ('up', 'Up'),
        ('down', 'Down'),
        ('stopped', 'Stopped'),
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='idle')
    current_floor = models.IntegerField(default=1)
    direction = models.CharField(
        max_length=20, choices=DIRECTION_CHOICES, default='stopped')

    def __str__(self):
        return f'Elevator {self.id}'


class Request(models.Model):
    floor = models.IntegerField()
    elevator = models.ForeignKey(
        Elevator, on_delete=models.CASCADE, related_name='requests')

    def __str__(self):
        return f'Request: Floor {self.floor} - Elevator {self.elevator_id}'
