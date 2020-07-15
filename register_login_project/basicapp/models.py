from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileIno(models.Model):
    #Create one to one connection with the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Creating new profile pic and url fields 
    profile_pic = models.ImageField(blank=True, upload_to = 'profile_pics')
    portfolio_url = models.URLField(blank=True)

    #Return username when model is called
    def __str__(self):
        return self.user.username

