from django.db import models

class Award(models.Model):
    name = models.CharField(max_length=100)

class Character(models.Model):
    name = models.CharField(max_length=100)

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Drama(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    seasons = models.IntegerField()

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
