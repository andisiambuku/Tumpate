from random import choices
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    image = models.ImageField(upload_to='missing_people')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    last_seen_date = models.DateField(default=timezone.now)
    last_seen_location = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
