# Generated by Django 3.2.4 on 2021-06-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='4B4D1', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
