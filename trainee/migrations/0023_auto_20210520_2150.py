# Generated by Django 3.1.7 on 2021-05-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0022_auto_20210520_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='A49B9', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
