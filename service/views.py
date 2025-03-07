from django.db.models import Q
from django.shortcuts import render, redirect
import pandas as pd
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Task
from .forms import TaskForm


class MainView(APIView):
    def get(self, request):
        return render(request, "main.html")


class AddDataView(APIView):
    def get(self, request):
        form = TaskForm()
        return render(request, "add_data.html", {"form": form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")


class ExportTasksAPIView(APIView):
    def get(self, request, *args, **kwargs):
        tasks = (
            Task.objects.select_related("project", "assigned_to").all().order_by("id")
        )

        data = [
            {
                "Project Name": task.project.project_name,
                "Task Name": task.name,
                "Assigned To": task.assigned_to.name,
                "Start Date": task.start_date.strftime("%Y-%m-%d"),
                "Days Required": task.days_required,
                "End Date": task.end_date.strftime("%Y-%m-%d"),
                "Progress": task.progress,
            }
            for task in tasks
        ]
        df = pd.DataFrame(data)
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = 'attachment; filename="tasks.xlsx"'

        with pd.ExcelWriter(response, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Tasks", index=False)

        return response


class TaskSearchView(APIView):
    def get(self, request):
        return render(request, "search.html", {"tasks": None})

    def post(self, request):
        query = request.POST.get("query")
        tasks = (
            Task.objects.filter(
                Q(name__icontains=query)
                | Q(project__project_name__icontains=query)
                | Q(start_date__icontains=query)
                | Q(end_date__icontains=query)
                | Q(days_required__icontains=query)
                | Q(progress__icontains=query)
                | Q(assigned_to__name__icontains=query)
            )
            if query
            else None
        )

        return render(request, "search.html", {"tasks": tasks, "query": query})
