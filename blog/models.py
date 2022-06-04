from django.db import models






class Post(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	file = models.FileField(upload_to='larg')
	date =  models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title

		
