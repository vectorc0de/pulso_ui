# Generated by Django 3.2.10 on 2022-01-10 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduino_check', '0012_auto_20220109_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='arduinolog',
            name='heart_rate',
            field=models.CharField(default=None, max_length=12),
            preserve_default=False,
        ),
    ]
