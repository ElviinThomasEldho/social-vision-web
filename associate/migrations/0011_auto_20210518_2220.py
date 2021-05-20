# Generated by Django 3.1.7 on 2021-05-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associate', '0010_auto_20210518_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='uniqueID',
            field=models.CharField(default='2227F', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='uniqueID',
            field=models.CharField(default='CFDC0', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='uniqueID',
            field=models.CharField(default='60F2E', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='uniqueID',
            field=models.CharField(default='BEA16', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
