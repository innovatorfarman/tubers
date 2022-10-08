from pickle import TRUE
from django.db import models

# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_id= models.IntegerField()
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.first_name