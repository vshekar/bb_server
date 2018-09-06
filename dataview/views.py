from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.
def check_login(request):
    response_data = {'login': "success", 'message': "Successfully logged in"}
    return JsonResponse(response_data)