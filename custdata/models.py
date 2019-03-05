from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Customers(models.Model):
	customer_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	address_1 = models.CharField(max_length=100, null=True, blank=True)
	address_2 = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=100, null=True, blank=True)
	zip_code = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)
	country_code = models.CharField(max_length=100, null=True, blank=True)
	origin_date = models.DateTimeField(default=datetime.now, null=True, blank=True) # date they first became a customer
	cust_email = models.EmailField(null=True, blank=True)
	cust_phone = models.CharField(max_length=20, null=True, blank=True)
	cust_media_origin = models.CharField(max_length=100, null=True, blank=True) # what media did the customer originally order from? DM, online, newspaper, etc.
	cust_notes = models.TextField(null=True, blank=True)

	# def __str__(self):
	# 	return f'{self.first_name} {self.last_name}'


class Orders(models.Model):
	customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)  # test this - try CASCADE too
	order_id = models.CharField(max_length=100, null=True, blank=True)
	product_id = models.CharField(max_length=100, null=True, blank=True)
	order_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
	unit_price = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
	order_total = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, null=True, blank=True)
	order_detail = models.TextField(max_length=100, null=True, blank=True)
	refunded = models.BooleanField(null=True, blank=True)
	refund_amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	ord_media_origin = models.CharField(max_length=100, null=True, blank=True)  # what media generated the order? DM, online, newspaper, etc.
	camp_id	= models.CharField(max_length=100, null=True, blank=True)  # foreign key
# shipping_cost

	# def __str__(self):
	# 	return self.title

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})
