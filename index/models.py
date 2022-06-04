from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Announcement(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True, default="Your announcement content here")
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete='CASCADE', null=True)

	def __str__(self):
		return self.title

