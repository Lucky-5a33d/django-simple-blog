from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField("date published")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", args=(str(self.id)))
