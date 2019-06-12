from django.db import models

# Create your models here.

class Node(models.Model):
    name = models.CharField(max_length=20)
    from_to = models.CharField(max_length=50)

    def __str__(self):
        return self.name
