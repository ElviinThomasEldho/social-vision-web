# Generated by Django 3.1.7 on 2021-05-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('changemaker', '0026_auto_20210526_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changemaker',
            name='uniqueID',
            field=models.CharField(default='129FA', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='uniqueID',
            field=models.CharField(default='CC1E0', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='studentID'),
        ),
    ]
