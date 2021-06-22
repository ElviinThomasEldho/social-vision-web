# Generated by Django 3.2.4 on 2021-06-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='uniqueID',
            field=models.CharField(default='0D57D', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='uniqueID',
            field=models.CharField(default='40A4C', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='uniqueID',
            field=models.CharField(default='9DAC7', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='uniqueID',
            field=models.CharField(default='FEFCC', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]