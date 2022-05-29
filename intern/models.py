from django.db import models

# Create your models here.
class Intern(models.Model):
    name = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    year = models.CharField(max_length=12)
    company = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + " " + self.college + " " + self.year + " " + self.company
    