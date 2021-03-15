from django.db import models


class Country(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class City(models.Model):

    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name


class Person(models.Model):
    peron_name = models.CharField(max_length=200)
    country=models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.peron_name


