from django.db import models

class CreateElection(models.Model):
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    date=models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.type}'
