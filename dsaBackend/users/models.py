from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
    

# class Solution(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='solutions')
#     created_at = models.DateTimeField(auto_now_add=True)
#     notes = models.TextField(blank=True, null=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"Solution by {self.user.username} at {self.created_at}"