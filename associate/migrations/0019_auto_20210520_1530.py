# Generated by Django 3.1.7 on 2021-05-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associate', '0018_auto_20210520_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='uniqueID',
            field=models.CharField(default='54442', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='uniqueID',
            field=models.CharField(default='A1922', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='uniqueID',
            field=models.CharField(default='2456B', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='uniqueID',
            field=models.CharField(default='8D392', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]