from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class MainView(APIView):
    def get(self, request,):
        return render(request,'main.html')