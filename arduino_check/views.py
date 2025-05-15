import datetime
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.template import loader
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from arduino_check.models import Patient, ArduinoLog


def get_short_date(total_seconds):
    mins = total_seconds / 60
    hrs = mins / 60
    days = hrs / 24
    weeks = days / 7
    month = weeks / 4
    years = month / 12

    if years > 1:
        return str(int(years)) + "Y"

    elif month > 1:
        return str(int(month)) + "M"

    elif weeks > 1:
        return str(int(weeks)) + "W"        

    elif days > 1:
        return str(int(days)) + "D"        

    elif hrs > 1:
        return str(int(hrs)) + "H"


    elif month > 1:
        return str(int(month)) + "M"

    elif mins > 1:
        return "Just now"


# str_response = "JAJAJAJAJAJAJA " + str(patient_id) + " - " + str(value_to_search) + " " + logic_operator + " " + multipler
def get_patients_reports(request, patient_id, value_to_search, multipler, logic_operator):
    arduino_logs = ArduinoLog.objects.filter(patient_id=patient_id).order_by(("-log_date"))
    i = 0

    ret_list = []

    for cal in arduino_logs:
        simple_dt = cal.log_date.replace(tzinfo=None)
        delta = datetime.datetime.now() - simple_dt
        final_delta = get_short_date(delta.total_seconds())
        
        ret_list.append({
            "hr": cal.heart_rate, 
            "spo2": cal.spo2,
            "finalDelta": final_delta
            })

    return JsonResponse({'dats': ret_list})

def statistics_view(request):
    return render(request, 'statistics.html', {})


def get_patients_options(request):
    grouped_patients = Patient.objects.values_list("first_name", "id")
    return JsonResponse({'patients': list(grouped_patients)})


def index(request):
    template = loader.get_template('test/index.html')    
    context = {}
    return HttpResponse(template.render(context, request))