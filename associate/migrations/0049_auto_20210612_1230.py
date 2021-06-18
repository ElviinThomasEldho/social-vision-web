# Generated by Django 3.1.7 on 2021-06-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associate', '0048_auto_20210608_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associate',
            name='uniqueID',
            field=models.CharField(default='1B83A', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='uniqueID',
            field=models.CharField(default='82937', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='uniqueID',
            field=models.CharField(default='82C8F', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='uniqueID',
            field=models.CharField(default='BF1EF', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
