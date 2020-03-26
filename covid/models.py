from django.db import models

# Create your models here.


class covid19_tb(models.Model):
    update_id = models.AutoField(primary_key=True)
    Country = models.CharField(max_length=30)
    total_cases = models.IntegerField(max_length=30)
    today_cases = models.IntegerField(max_length=30)
    total_deaths = models.IntegerField(max_length=30)
    today_deaths = models.IntegerField(max_length=30)
    recovered = models.IntegerField(max_length=30)
    active = models.IntegerField(max_length=30)
    critical = models.IntegerField(max_length=30)

    def __str__(self):
        return self.Country


class all_covid(models.Model):
    all_id = models.AutoField(primary_key=True)
    Cases_all = models.IntegerField(max_length=30)
    Deaths = models.IntegerField(max_length=30)
    Recovered = models.IntegerField(max_length=30)

    def __str__(self):
        return self.Cases_all