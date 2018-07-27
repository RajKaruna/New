from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class List(models.Model):
	item=models.CharField(max_length=200, default="")
	completed=models.BooleanField(max_length=200, default=False)
	date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	

def __str__(self):
	return self.item + '|' + str(self.completed)












