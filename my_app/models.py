from django.db import models


# Create your models here.
class AllBlock(models.Model):
    number_block = models.CharField(max_length=100)
    cost_apart = models.CharField(max_length=100)
    number_kol = models.CharField(max_length=100)
    floor_kol = models.CharField(max_length=100)
    num_apart_per_floor = models.CharField(max_length=100)


class Owner(models.Model):
    two_choices = [
        ('Выкуп', 'Выкуп'),
        ('Выкуп не до конца', 'Выкуп не до конца'),
        ('Расторгнуто', 'Расторгнуто'),
        ("Не продано", "Не продано"),
    ]
    fio = models.CharField(max_length=100, null=True, blank=True, default='--Без-хоз--')
    data_sales = models.DateField()
    status = models.CharField(max_length=100, choices=two_choices)
    block = models.CharField(max_length=100)
    total_area = models.CharField(max_length=100)
