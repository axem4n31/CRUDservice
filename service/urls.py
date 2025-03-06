from django.urls import path

from service.views import MainView

urlpatterns = [
    path("", MainView.as_view(), name="main")
]