# Generated by Django 3.2.16 on 2023-08-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20230823_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisresult',
            name='app',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='analysisresult',
            name='report',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
