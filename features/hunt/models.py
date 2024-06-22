from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

CLASS_CHOICES=[
    ('KNIGHT', 'Guerreiro'),
    ('SORCERER', 'Feiticeiro'),
    ('DRUID', 'Druida'),
    ('PALADIN', 'Paladino'),
]

# Create your models here.

class Hunt(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50,null=False, blank=False)
    level_min = models.IntegerField(null=False, blank=False,validators=[MinValueValidator(1)])
    level_max = models.IntegerField(null=False, blank=False,validators=[MinValueValidator(level_min)])
    class_type = models.CharField(max_length=50, null=False, blank=False)

    def clean(self):
        if self.level_max < self.level_min:
            raise ValidationError({'level_max': 'O nível máximo não pode ser menor que o nível mínimo.'})

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)  

    def __str__(self):
        return self.name