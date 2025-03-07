import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from service.models import Worker, Project, Task
from datetime import datetime


class Command(BaseCommand):
    help = "Импорт данных из Excel в базу данных"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Путь к файлу Excel")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        self.stdout.write(self.style.SUCCESS(f"Импорт данных из {file_path}..."))

        try:
            df = pd.read_excel(file_path, sheet_name="Project Management Data")

            with transaction.atomic():
                for _, row in df.iterrows():
                    project, _ = Project.objects.get_or_create(
                        project_name=row["Project Name"]
                    )
                    worker, _ = Worker.objects.get_or_create(name=row["Assigned to"])

                    Task.objects.create(
                        name=row["Task Name"],
                        project=project,
                        start_date=pd.to_datetime(row["Start Date"]).date(),
                        end_date=pd.to_datetime(row["End Date"]).date(),
                        days_required=int(row["Days Required"]),
                        progress=int(row["Progress"] * 100),
                        assigned_to=worker,
                    )

            self.stdout.write(self.style.SUCCESS("Импорт завершен!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка импорта: {e}"))
