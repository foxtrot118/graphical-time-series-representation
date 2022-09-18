import joblib
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .models import Sales, Client, Employee,Returns,Values
from .serializers import SalesSerializer, ClientSerializer, EmployeeSerializer, ReturnsSerializer, ValuesSerializer


import pandas as pd
import numpy as np
from pandas import read_csv
from pmdarima.arima import auto_arima
from datetime import datetime
import matplotlib.pyplot as plt
from pmdarima.arima import ADFTest


class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SalesView(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    allowed_methods = ['post']

class ValuesView(viewsets.ModelViewSet):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer 

class ReturnsView(viewsets.ModelViewSet):
    queryset = Returns.objects.all()
    serializer_class = ReturnsSerializer    


class FileUploadView(views.APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, filename, format=None):
        file_obj = request.data['file']
       

        sales = read_csv(file_obj)
       

        sales['Month'] = pd.to_datetime(sales['Month'], errors = 'coerce')
        sales.set_index('Month', inplace=True)

        adf_test = ADFTest(alpha=0.05)
        adf_test.should_diff(sales)