from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Message(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	text = models.TextField()
	send_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.author} - {self.send_at} - {self.text}'