from django.db import models

# Company models here.

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT',"IT"),
                                                  ('Non IT',"Non IT"),
                                                  ("Mobiles phones","Mobile phones")
                                                  ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


#employee Model here

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(("Manager",'manager'),
                                                     ('Software Developer','sd'),
                                                     ('Project Leader','pl')
                                                     ))
    
    company=models.ForeignKey(Company,on_delete=models.CASCADE)  # is se pata chalega kaun sa employee kis company me hai



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
