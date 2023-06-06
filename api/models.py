from datetime import datetime
from django.db import models



#leetcode model here
class Leetcode(models.Model):
    
    name = models.CharField(max_length=500)
    url = models.URLField()
    duration = models.IntegerField()
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    in_24_hours = models.BooleanField()
    
    # The primary_key argument is set to None to prevent Django from creating an `id` field.
    primary_key = None

    def __str__(self):
        return self.name


#CodeChefC model here
class CodeChef(models.Model):
    
    name = models.CharField(max_length=500)
    url = models.URLField()
    duration = models.IntegerField()
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    in_24_hours = models.BooleanField()
    
    # The primary_key argument is set to None to prevent Django from creating an `id` field.
    primary_key = None

    def __str__(self):
        return self.name
