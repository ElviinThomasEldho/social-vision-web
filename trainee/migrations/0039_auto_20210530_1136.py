# Generated by Django 3.1.7 on 2021-05-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0038_auto_20210530_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='294FE', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]