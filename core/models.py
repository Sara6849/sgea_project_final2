from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Aluno'),
        ('teacher', 'Professor'),
        ('organizer', 'Organizador'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
<<<<<<< HEAD
    phone = models.CharField(max_length=15, blank=True, null=True)
=======
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793

    def __str__(self):
        return self.username

<<<<<<< HEAD

=======
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('workshop', 'Workshop'),
        ('lecture', 'Palestra'),
        ('seminar', 'Seminário'),
    )
    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    max_participants = models.PositiveIntegerField()
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
<<<<<<< HEAD
    participants = models.ManyToManyField(User, related_name='events_participated', blank=True)
    banner = models.ImageField(upload_to='event_banners/', null=True, blank=True)
=======
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793

    def __str__(self):
        return self.title

<<<<<<< HEAD

=======
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_issued = models.DateTimeField(auto_now_add=True)

=======
>>>>>>> d777e06a7afec3224da65659784b0ef318e76793
    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"
