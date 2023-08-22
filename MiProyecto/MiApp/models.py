from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    materia = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.materia}"

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    escuela = models.CharField(max_length=100)
    mail = models.EmailField()
    def __str__(self):
        return f"{self.nombre}, {self.escuela}, {self.mail}"


class Preceptor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.curso}"

