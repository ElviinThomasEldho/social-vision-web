# Generated by Django 3.1.7 on 2021-05-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0015_auto_20210519_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='5F1B6', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]