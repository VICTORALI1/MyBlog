from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view',kwargs={'pk':self.pk})
