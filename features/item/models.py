from django.db import models

ITEM_CHOICES=[
    ('WEAPON', 'Arma'),
    ('Shield', 'Escudo')
    ('RING', 'Anel'),
    ('AMULET', 'Amuleto'),
    ('BOOTS', 'Botas'),
    ('HELMET', 'Capacete'),
    ('SHIELD', 'Escudo'),
    ('LEGGINGS', 'Calças'),
    ('CHESTPLATE', 'Peitoral'),
    ('NECKLACE', 'Colar'),
]

CLASS_CHOICES=[
    ('KNIGHT', 'Guerreiro'),
    ('SORCERER', 'Feiticeiro'),
    ('DRUID', 'Druida'),
    ('PALADIN', 'Paladino'),
]

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    item_type = models.CharField(choices=ITEM_CHOICES, null=False, blank=False)
    class_type = models.CharField(choices=CLASS_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.name
