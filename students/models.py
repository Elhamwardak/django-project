from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    course = models.CharField(max_length=120)
    is_passed = models.BooleanField(default=True)
    last_name = models.CharField(max_length=80)
    address = models.TextField(null=True, blank=True)
    joined_on = models.DateTimeField()
    


    def __str__(self):
        # return self.name +" - "+ str(self.id)
        return f"{self.name}-{self.id}"
