# Generated by Django 5.1.6 on 2025-03-06 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("project_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Worker",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("days_required", models.IntegerField()),
                ("progress", models.IntegerField()),
                (
                    "project_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="service.project",
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="service.worker"
                    ),
                ),
            ],
        ),
    ]
