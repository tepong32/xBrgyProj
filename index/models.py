from django.db import models

# Create your models here.

class Announcement(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True, default="Your content here")
	date_posted = models.DateTimeField(auto_now_add=True)

