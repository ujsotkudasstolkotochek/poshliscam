from django.db import models

class Rabotnichki(models.Model):
    name = models.CharField(max_length = 999, blank = False)
    second_name = models.CharField(max_length = 999, blank = True)
    third_name = models.CharField(max_length = 999, blank = True)
    selery = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.name} {self.second_name}'
