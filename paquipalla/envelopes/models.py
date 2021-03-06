from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name)


class Envelope(models.Model):
    amount = models.IntegerField()
    motive = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.company.name, self.motive)
