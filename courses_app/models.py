from django.db import models
import datetime

# Create your models here.

# This is for validation:
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors["desc"] = "Course description should be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_added = models.DateField(default=datetime.datetime.now)
    objects = CourseManager()