# Generated by Django 3.1.7 on 2021-05-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0024_auto_20210524_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='course',
            new_name='enrolledCourses',
        ),
        migrations.RemoveField(
            model_name='trainee',
            name='currentCourse',
        ),
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='282AB', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]
