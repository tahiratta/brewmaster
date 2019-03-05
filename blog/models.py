# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.urls import reverse
#
#
# class Post(models.Model):
# 	title 		= models.CharField(max_length=100)
# 	content 	= models.TextField()
# 	date_posted = models.DateTimeField(default=timezone.now)
# 	author 		= models.ForeignKey(User, on_delete=models.CASCADE)
#
# 	def __str__(self):
# 		return self.title
#
# 	def get_absolute_url(self):
# 		return reverse('post-detail', kwargs={'pk': self.pk})

from django.db import models

class Document(models.Model):
    document = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.id