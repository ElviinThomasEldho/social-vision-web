# Generated by Django 3.1.7 on 2021-05-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('desc', models.CharField(max_length=256, null=True)),
                ('date', models.DateField(null=True)),
                ('image1', models.ImageField(null=True, upload_to='')),
                ('image2', models.ImageField(null=True, upload_to='')),
                ('image3', models.ImageField(null=True, upload_to='')),
                ('image4', models.ImageField(null=True, upload_to='')),
                ('image5', models.ImageField(null=True, upload_to='')),
                ('image6', models.ImageField(null=True, upload_to='')),
                ('image7', models.ImageField(null=True, upload_to='')),
                ('image8', models.ImageField(null=True, upload_to='')),
                ('image9', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
