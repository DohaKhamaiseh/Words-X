from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Word(models.Model):
    word= models.CharField(max_length=255, null=False)
    User = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    comment=models.TextField(default="Write your comment")

    def get_absolute_url(self):
        return reverse("word_detail", args=[str(self.id)])