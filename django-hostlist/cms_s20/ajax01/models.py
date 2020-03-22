from django.db import models

# Create your models here.


class ajax_User(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=0)
    # pwd=models.CharField(max_length=32)

class ajax_UserInfo(models.Model):
    user=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)