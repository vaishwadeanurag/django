from django.db import models
# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length = 200)
	company = models.CharField(max_length = 300)
	email = models.EmailField()
	contact_no = models.IntegerField(max_length = 10)
	project_name = models.CharField(max_length = 200)
	project_info = models.TextField(max_length = 1000)

	def __unicode__(self):
		return self.name