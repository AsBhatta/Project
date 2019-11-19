from django.db import models

class user_profile(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=15)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.username
