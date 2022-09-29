from email.policy import default
from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=250)
    data = models.TextField()
    value = models.IntegerField()
    completed = models.BooleanField(default=False)
    val1 = models.BooleanField(default = True)
    def __str__(self):
        return self.name