from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    datecontra = models.DateField(null=True, blank=True)
    anotado = models.BooleanField(default=False)
    diasanotados = models.PositiveIntegerField(default=0)
    tiex = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ' Fecha de fin de contrato' 
    