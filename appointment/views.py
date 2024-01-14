from django.shortcuts import render
from rest_framework import viewsets
from .models import Appoinment
from .serializers import AppoinmentSerializer


class AppoinmentViewSet(viewsets.ModelViewSet):
    queryset = Appoinment.objects.all()
    serializer_class = AppoinmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # print(self.request.query_params)

        patient_id = self.request.query_params.get('patient_id')

        if patient_id:
            queryset = queryset.filter(patient_id = patient_id)
        return queryset
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # print(self.request.query_params)

        doctor_id = self.request.query_params.get('doctor_id')

        if doctor_id:
            queryset = queryset.filter(doctor_id = doctor_id)
        return queryset

