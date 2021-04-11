from django.db import models
from datetime import datetime

class Hospital_Type(models.Model):
    type_name = models.CharField(max_length=50)
    region = models.TextField()
    contact_no = models.IntegerField()
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.type_name


class Hospital(models.Model):
    hospital_id = models.IntegerField()
    category = models.ForeignKey(Hospital_Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    slug = models.SlugField(max_length=50)
    address = models.TextField()
    updated_date = models.DateTimeField(default=datetime.now)
    logo = models.ImageField(upload_to='media/hospital/', blank=True, null=True)

    def __str__(self):
        return self.name
