# Generated by Django 3.1.7 on 2021-05-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_auto_20210510_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='CA8FF', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
