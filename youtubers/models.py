from asyncio.windows_events import NULL
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Youtuber(models.Model):
    city_choices = [
        ('Delhi', 'Delhi'),
        ('Jaipur', 'Jaipur'),
        ('Mumbai', 'Mumbai'),
        ('Gurugram','Gurugram'),
    ]

    category_choices = [
        ('Coding','coding'),
        ('Vlogs','vlogs'),
        ('Education','education'),
        ('Reviews','reviews'),
    ]

    crew_choices = [
        ('solo', 'solo'),
        ('small','small'),
        ('large', 'large'),
    ]
    camera_choices = [
        ('canon','canon'),
        ('nikon','nikon'),
        ('panasonic','panasonic'),
        ('fuji','fuji'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    description = RichTextField()
    price = models.IntegerField()
    subs_count = models.IntegerField()
    camera = models.CharField(choices = camera_choices, max_length=255, default='NA' )
    crew = models.CharField(choices = crew_choices, max_length=50)
    category = models.CharField(choices = category_choices, max_length=255)
    city = models.CharField(choices = city_choices, max_length=255)
    state = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    video = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'media/youtubers/%Y/%m/%d/')
    created_date = models.DateTimeField(default = datetime.now(), blank = True)

    def __str__(self):
        return self.first_name