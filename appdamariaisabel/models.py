from django.db import models

class Hobbies (models.Model):
  OPTIONS = [
    ("N","Never"),
    ("S","Sometimes"),
    ("A","Always"),
  ]
  
  title = models.CharField(max_length=50)
  practice_duration = models.CharField(max_length=70)
  frequency = models.CharField(max_length=1,choices=OPTIONS,default="")
  benefits = models.CharField(max_length=150)

class Learn(models.Model): 
  CATEGORY = [
    ("F","Fun"),
    ("W","Work"),
    ("H","Health"),
  ]
  title = models.CharField(max_length=70)
  category = models.CharField(max_length=1, choices= CATEGORY, default="")
  priority = models.IntegerField()
  current_level = models.CharField(max_length=70)


  