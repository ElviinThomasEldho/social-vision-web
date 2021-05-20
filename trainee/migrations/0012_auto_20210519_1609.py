# Generated by Django 3.1.7 on 2021-05-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0011_auto_20210518_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.IntegerField(null=True, verbose_name='Duration (in months)'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='DBD27', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
