from django.conf import settings
from django.db import models
# from django.conf.auth.models import User
from django.contrib.auth.models import User

# Create your models here.
class Wedding(models.Model):
	# id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True, db_column='id')
	# id = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True, db_column='id', unique=True)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE, db_column='user_id')
	my_name = models.TextField(default='')
	your_name = models.TextField(default='')

	my_gender = models.BooleanField(default=0)
	your_gender = models.BooleanField(default=0)

	myfather_name = models.TextField(null=True,default='')
	mymother_name = models.TextField(null=True,default='')

	yourfather_name = models.TextField(null=True,default='')
	yourmother_name = models.TextField(null=True,default='')

	wedding_location = models.TextField(default='')
	wedding_date = models.TextField(default='')
	wedding_photo = models.TextField(null=True,default='')