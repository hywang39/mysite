from django.db import models

# Create your models here.
class Restaurant(models.Model):
    class Meta:
        db_table = 'Restaurant'

    restaurant_id = models.IntegerField(primary_key=True);
    restaurant_name = models.CharField(max_length=50);
    restaurant_open_hour = models.BigIntegerField();
    restaurant_close_hour = models.BigIntegerField();
    restaurant_address = models.CharField(max_length=50);
    restaurant_phone = models.CharField(max_length=20);
    restaurant_email = models.CharField(max_length=50);
    restaurant_category = models.CharField(max_length=20);
    restaurant_description = models.CharField(max_length=300, null=True);
    restaurant_score = models.FloatField();
    restaurant_area = models.CharField(max_length=20);
    restaurant_revenue = models.FloatField();
    restaurant_num_recommendation = models.IntegerField();
    restaurant_picture = models.CharField(max_length=50);

class DBVersion(models.Model):
    class Meta:
        db_table = 'dbversion'

    id = models.IntegerField(primary_key = True)
    develop_version = models.IntegerField()
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
