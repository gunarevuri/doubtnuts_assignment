from django.db import models
from django.contrib.auth.models import User

class_choices = [(6,6), (7,7), (8,8), (9,9), (10,10), (11,11), (12,12)]

class user(models.Model):
	first_name = models.CharField("User First Name", max_length=50)
	last_name = models.CharField("User Last Name", max_length=50)
	address = models.CharField("Address", max_length=300)
	pincode = models.IntegerField("Pin Code", )


class Class(models.Model):
	class_section = models.IntegerField("Class ", choices = class_choices )
	def __str__(self):
		return f"class {self.class_section}"


class VideoSolutions(models.Model):
	title = models.CharField("Solution Title", max_length=30)
	class_section = models.IntegerField("Class", choices=class_choices)
	video = models.FileField(upload_to="class/", verbose_name='Upload Video', null=True,blank=True)
	def __str__(self):
		return f"{self.title}"
