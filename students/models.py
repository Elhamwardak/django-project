from django.db import models
from django.forms import ValidationError

# Create your models here.

COURSES  = [
    ("001", "python"),
    ("002", "javasvript"),
]

def min_age(val):
    if val < 18:
        raise ValidationError("Age should be greater than 18")


class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(validators=[min_age])
    course = models.CharField(max_length=120, choices = COURSES)
    is_passed = models.BooleanField(default=True)
    last_name = models.CharField(max_length=80)
    address = models.TextField(null=True, blank=True)
    joined_on = models.DateTimeField()
    


    def __str__(self):
        # return self.name +" - "+ str(self.id)
        return f"{self.name}-{self.id}"



