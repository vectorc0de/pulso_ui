# Generated by Django 3.1.6 on 2022-01-12 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arduino_check', '0014_auto_20220112_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArduinoLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spo2', models.CharField(max_length=12)),
                ('heart_rate', models.CharField(max_length=12)),
                ('log_date', models.DateTimeField(verbose_name='log date')),
                ('arduino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arduino_check.arduino')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arduino_check.patient')),
            ],
        ),
    ]
