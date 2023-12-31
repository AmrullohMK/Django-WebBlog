from django.db import models
from django.contrib.auth.models import User
from PIL import Image  
#import the pillow image library

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    date_opened =models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    #Overiding save meethod to resize images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
        

    
    