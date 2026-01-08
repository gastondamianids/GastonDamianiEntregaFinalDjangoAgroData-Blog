from django.db import models
from django.contrib.auth.models import User
from pages.models import Page

class Comment(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username}"
# Create your models here.
