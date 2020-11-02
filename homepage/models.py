from django.db import models
from django.contrib.auth.models import User
class post(models.Model):
    uname=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField(blank=True)