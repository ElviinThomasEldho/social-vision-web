# Generated by Django 3.1.7 on 2021-05-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changemaker', '0010_auto_20210518_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changemaker',
            name='uniqueID',
            field=models.CharField(default='4FA3D', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='uniqueID',
            field=models.CharField(default='20BB8', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='studentID'),
        ),
    ]
