# Generated by Django 3.1.7 on 2021-05-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changemaker', '0013_auto_20210519_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changemaker',
            name='uniqueID',
            field=models.CharField(default='93A34', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='uniqueID',
            field=models.CharField(default='8E744', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='studentID'),
        ),
    ]