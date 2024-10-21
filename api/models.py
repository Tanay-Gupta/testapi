from django.db import models




#---------------------------------------------------------------Sites model here------------------------------------------------------------
class CodingPlatform(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    url = models.URLField()
    def __str__(self):
        return self.name


#---------------------------------------------------------------AllContest model here------------------------------------------------------------
class AllContests(models.Model):
    
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


#---------------------------------------------------------------Leetcode model here------------------------------------------------------------
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



#---------------------------------------------------------------CodeChef model here------------------------------------------------------------
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


#---------------------------------------------------------------Codeforces model here------------------------------------------------------------
class Codeforces(models.Model):
    
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


#---------------------------------------------------------------HackerRank model here------------------------------------------------------------
class HackerRank(models.Model):
    
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


#---------------------------------------------------------------HackerEarth model here------------------------------------------------------------
class HackerEarth(models.Model):
    
    name = models.CharField(max_length=500)
    url = models.URLField()
    duration = models.IntegerField()
    start_time = models.CharField(max_length=50)
    type=models.TextField(default='contest')
    end_time = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    in_24_hours = models.BooleanField()
    
    
    # The primary_key argument is set to None to prevent Django from creating an `id` field.
    primary_key = None

    def __str__(self):
        return self.name
    def __str__(self):
        return self.contest_type


#---------------------------------------------------------------CSAcademy model here------------------------------------------------------------
class CSAcademy(models.Model):
    
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

#---------------------------------------------------------------AtCoder model here------------------------------------------------------------
class AtCoder(models.Model):
    
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

#---------------------------------------------------------------TopCoder model here------------------------------------------------------------
class TopCoder(models.Model):
    
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

#---------------------------------------------------------------CodeForcesGym model here------------------------------------------------------------
class CodeForcesGym(models.Model):
    
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

#---------------------------------------------------------------Geekforgeeks model here------------------------------------------------------------
class Geekforgeeks(models.Model):
    
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



#---------------------------------------------------------------CodingNinjas model here------------------------------------------------------------
class CodingNinjas(models.Model):
    
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