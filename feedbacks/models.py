from django.db import models
from django.core.urlresolvers import reverse_lazy
# Create your models here.

class Feedback(models.Model):
	name = models.CharField(max_length=255)
	subject = models.TextField(max_length=255)
	message = models.TextField()
	from_email = models.EmailField()
	create_date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.name