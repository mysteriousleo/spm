from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_control
import os
import joblib

model1 = joblib.load(os.path.dirname(__file__) + "\\myModel2SVC.pkl")
model2 = joblib.load(os.path.dirname(__file__) + "\\model1.pkl")

# Create your views he
def index(request):
    return render(request, 'index.html')


def checkSpam(request):
    return render(request,'output.html')