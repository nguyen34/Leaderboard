from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'address': self.address,
            'points': self.points
        }
