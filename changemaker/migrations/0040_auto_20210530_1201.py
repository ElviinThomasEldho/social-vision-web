# Generated by Django 3.1.7 on 2021-05-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changemaker', '0039_auto_20210530_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changemaker',
            name='uniqueID',
            field=models.CharField(default='BAC01', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='uniqueID',
            field=models.CharField(default='66541', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='studentID'),
        ),
    ]
