from django.db import models

class Fan(models.Model):
    fan_nomi = models.CharField(max_length=150, blank=True)
    imthon_joyi = models.TextField(blank=True)
    oqituvchi = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        return self.fan_nomi


class Savollar(models.Model):
    savol = models.TextField(blank=True) 
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.savol
    

