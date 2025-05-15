from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('patients/filter-options/', views.get_patients_options, name='patients-filter-options'),
    path('patients/report/<int:patient_id>/<str:multipler>/<str:logic_operator>/<int:value_to_search>', views.get_patients_reports, name='p4tients-filter-options'),
]