# Generated by Django 3.1.7 on 2021-05-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associate', '0038_auto_20210530_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='uniqueID',
            field=models.CharField(default='37800', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='uniqueID',
            field=models.CharField(default='BDB93', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='uniqueID',
            field=models.CharField(default='41BEA', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='uniqueID',
            field=models.CharField(default='66932', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]