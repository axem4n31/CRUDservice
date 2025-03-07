from django.urls import path

from service.views import MainView, AddDataView, ExportTasksAPIView, TaskSearchView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("add-data/", AddDataView.as_view(), name="add_data"),
    path("export-tasks/", ExportTasksAPIView.as_view(), name="export_tasks"),
    path("search/", TaskSearchView.as_view(), name="search"),
]
