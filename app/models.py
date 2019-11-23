from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Pet (models.Model):
    cidade = models.CharField(max_length=100)
    descricao = models.TextField()
    fone = models.CharField(max_length=11)
    email = models.EmailField()
    imagem = models.ImageField(upload_to='pet')
    begin_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pet'



