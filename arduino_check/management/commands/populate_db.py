import string
import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

from arduino_check.models import Patient, Arduino, ArduinoLog

class Command(BaseCommand):
    help_patients = 'Populates the database with random generated data.'


    def add_arguments(self, parser):
        parser.add_argument('--patient', type=int, help='The number of pacient that should be created.')
        parser.add_argument('--arduino', type=int, help='The number of arduinos that should be created.')
        parser.add_argument('--logs', type=int, help='The number of logs that should be created.')


    def insert_arduino(self, cant):
        for i in range(cant):
            one_patient = Patient.objects.values("id").order_by('?')[:1]
            patient_obj = Patient.objects.get(id=one_patient[0]["id"])
            max_len = 10
            a = Arduino(patient=patient_obj, arduino_id=''.join(random.choices(string.ascii_uppercase + string.digits, k=max_len)))
            a.save()


    def insert_patient(self, cant):
        names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles']
        last_name = ['Smith', 'Jones', 'Taylor', 'Brown', 'Williams', 'Wilson', 'Johnson', 'Davies', 'Patel', 'Wright']
        # max_len = 9

        seconds_counter = 1
        for i in range(cant):
            rnd_names = random.randint(0, len(names)-1)
            rnd_lastnames = random.randint(0, len(last_name)-1)
            p = Patient(first_name=names[rnd_names], last_name=last_name[rnd_lastnames], register_date=datetime.now() - timedelta(days=random.randint(0, seconds_counter)))
            seconds_counter += 1
            p.save()        

    def insert_logs(self, cant):
        for i in range(cant):
            one_patient = Patient.objects.values("id").order_by('?')[:1]
            patient_obj = Patient.objects.get(id=one_patient[0]["id"])

            one_arduino = Arduino.objects.values("id").order_by('?')[:1]
            
            al = ArduinoLog(patient=patient_obj, 
                arduino_id=one_arduino, 
                spo2=random.uniform(10.5, 305.5), 
                heart_rate=random.uniform(10.5, 99.5), 
                log_date=datetime.now() - timedelta(days=random.randint(0, 1825)))

            al.save()



    def handle(self, *args, **options):
        if 'arduino' in options:
            if options['arduino'] is not None:
                self.insert_arduino(options['arduino'])

        if 'patient' in options:
            if options['patient'] is not None:
                self.insert_patient(options['patient'])

        if 'logs' in options:
            if options['logs'] is not None:
                self.insert_logs(options['logs'])