from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

GENDER_CHOICES = {
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHER'),
}



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/users/")
    biodata = models.TextField(max_length=300, blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True, null=True)
    birthdate = models.DateField(default=datetime.now, blank=True, null=True)