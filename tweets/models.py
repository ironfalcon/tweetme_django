import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='image/', blank=True, null=True)

    # def __str__(self):
    #     return self.content
    
    class Meta:
        ordering = ["-id"]
    
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 299)
        }
