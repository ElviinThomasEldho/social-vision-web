# Generated by Django 3.1.7 on 2021-05-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0012_auto_20210519_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='trainee',
            name='uniqueID',
            field=models.CharField(default='2E5DD', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID'),
        ),
    ]