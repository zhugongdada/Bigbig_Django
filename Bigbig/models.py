from django.db import models


# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

