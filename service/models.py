from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    project_name = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    days_required = models.IntegerField()
    progress = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    assigned_to = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name},  {self.project.project_name}"
