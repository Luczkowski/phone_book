from django.db import models


class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.CASCADE, null=True)
    telefon = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.telefon}"


class Email(models.Model):
    osoba = models.ForeignKey(Osoba, editable=False, on_delete=models.CASCADE, null=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"
