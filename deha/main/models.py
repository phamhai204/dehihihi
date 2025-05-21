from django.db import models
from django.contrib.auth.models import User

class Barber(models.Model):
    name = models.CharField(max_length=100)
    experience = models.TextField()
    photo = models.ImageField(upload_to='barbers/')
    schedule = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    barber = models.ForeignKey(Barber, on_delete=models.SET_NULL, null=True, blank=True)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} with {self.barber.name if self.barber else 'No Barber'} on {self.appointment_date.strftime('%Y-%m-%d %H:%M')}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.phone_number}"