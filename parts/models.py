from django.db import models
from django.contrib.auth.models import User


class Part(models.Model):
    part_title = models.CharField(max_length=200)
    composer_name = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)
    instrument = models.ForeignKey("Instrument", on_delete=models.CASCADE)
    level = models.ForeignKey("Level", on_delete=models.CASCADE)
    style = models.ForeignKey("Style", on_delete=models.CASCADE)
    curso = models.ForeignKey("Curso", on_delete=models.CASCADE)
    pdf = models.URLField(max_length=200)
    audio = models.URLField(max_length=200)
    student = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.part_title} -- {self.composer_name}"


class Instrument(models.Model):
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return self.instrument


class Level(models.Model):
    level = models.CharField(max_length=30)

    def __str__(self):
        return self.level


class Style(models.Model):
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.style


class Curso(models.Model):
    curso = models.CharField(max_length=30)

    def __str__(self):
        return self.curso
