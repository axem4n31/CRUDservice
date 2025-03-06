from django.db import models


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)


class Task(models.Model):
    name = models.CharField(max_length=50)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    days_required = models.IntegerField()
    progress = models.IntegerField()
    assigned_to = models.ForeignKey(Worker, on_delete=models.CASCADE)



