# Generated by Django 3.2.16 on 2023-09-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20230904_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysisresult',
            name='general_report',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='analysisresult',
            name='overall_report',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='analysisresult',
            name='personality_report',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='analysisresult',
            name='recommendations',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
