# Generated by Django 3.1.7 on 2021-05-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0033_auto_20210526_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='65F2A', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
