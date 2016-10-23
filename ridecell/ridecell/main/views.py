from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt


@xframe_options_exempt
@csrf_exempt
def home(request):
    return render(request, "main/home.html")
