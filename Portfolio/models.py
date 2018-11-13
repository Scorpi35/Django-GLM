from django.db import models

class Portfolio(models.Model):
    Category = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    P_Language = models.CharField(max_length=50)
    Github = models.CharField(max_length=300)
    Level = models.CharField(max_length=100)
