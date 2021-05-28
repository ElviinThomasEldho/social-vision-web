# Generated by Django 3.1.7 on 2021-05-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0026_auto_20210526_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='course',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainee.course'),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='EB9C8', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
