from django.conf import settings
from django.db import models
# from django.conf.auth.models import User
from django.contrib.auth.models import User

# Create your models here.
class Wedding(models.Model):
	# id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True, db_column='id')
	# id = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True, db_column='id', unique=True)
	user_id = models.ForeignKey(User,on_delete=models.CASCADE, db_column='user_id')
	my_name = models.TextField(null=True)
	your_name = models.TextField(null=True)

	my_gender = models.IntegerField(null=True)
	your_gender = models.IntegerField(null=True)

	myfather_name = models.TextField(null=True)
	mymother_name = models.TextField(null=True)

	yourfather_name = models.TextField(null=True)
	yourmother_name = models.TextField(null=True)

	wedding_location = models.TextField(null=True)
	wedding_date = models.TextField(null=True)
	wedding_photo = models.TextField(null=True)