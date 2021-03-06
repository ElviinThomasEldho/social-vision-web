# Generated by Django 3.2.4 on 2021-06-22 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('duration', models.IntegerField(null=True, verbose_name='Duration (in months)')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('uniqueID', models.CharField(default='9813F', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('profilePicture', models.ImageField(null=True, upload_to='', verbose_name='Profile Picture')),
                ('firstName', models.CharField(max_length=255, null=True, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=255, null=True, verbose_name='Last Name')),
                ('fatherName', models.CharField(max_length=255, null=True, verbose_name="Father's Name")),
                ('motherName', models.CharField(max_length=255, null=True, verbose_name="Mother's Name")),
                ('dateOfBirth', models.DateField(null=True, verbose_name='Date of Birth')),
                ('age', models.IntegerField(null=True, verbose_name='Age of Trainee')),
                ('bloodGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=255, null=True, verbose_name='Blood Group')),
                ('martialStatus', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Single', 'Single'), ('Widow', 'Widow')], max_length=255, null=True, verbose_name='Martial Status')),
                ('category', models.CharField(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('EWS', 'EWS')], max_length=255, null=True, verbose_name='Category')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=255, null=True, verbose_name='Gender')),
                ('religion', models.CharField(choices=[('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Sikh', 'Sikh'), ('Isai', 'Isai'), ('Jain', 'Jain'), ('Other', 'Other')], max_length=255, null=True, verbose_name='Religion')),
                ('mobileNumber', models.CharField(max_length=13, null=True, verbose_name='Mobile Number')),
                ('emailID', models.EmailField(max_length=254, null=True, verbose_name='Email Address')),
                ('emergencyContact', models.CharField(max_length=13, null=True, verbose_name='Emergency Contact')),
                ('occupation', models.CharField(choices=[('Private Job', 'Private Job'), ('Government Employee', 'Government Employee'), ('Self Employed', 'Self Employed'), ('House Wife', 'House Wife'), ('Business', 'Business')], max_length=255, null=True, verbose_name='Occupation')),
                ('education', models.CharField(choices=[('Nil', 'Nil'), ('5th Grade', '5th Grade'), ('6th Grade', '6th Grade'), ('7th Grade', '7th Grade'), ('8th Grade', '8th Grade'), ('9th Grade', '9th Grade'), ('10th Grade', '10th Grade'), ('11th Grade', '11th Grade'), ('12th Grade', '12th Grade'), ('Graduate', 'Graduate'), ('Post Graduate', 'Post Graduate')], max_length=255, null=True, verbose_name='Education')),
                ('address', models.CharField(max_length=512, null=True, verbose_name='Address')),
                ('area', models.CharField(max_length=255, null=True, verbose_name='Area')),
                ('locality', models.CharField(max_length=255, null=True, verbose_name='Locality')),
                ('district', models.CharField(max_length=255, null=True, verbose_name='District')),
                ('state', models.CharField(max_length=255, null=True, verbose_name='State')),
                ('pincode', models.CharField(max_length=255, null=True, verbose_name='Pincode')),
                ('documentType', models.CharField(choices=[('Aadhaar Card', 'Aadhaar Card'), ('Voter Card', 'Voter Card'), ('PAN Card', 'PAN Card'), ('Ration Card', 'Ration Card'), ('Passport', 'Passport'), ('Driving License', 'Driving License')], max_length=255, null=True, verbose_name='Document Type')),
                ('documentNumber', models.CharField(max_length=255, null=True, verbose_name='Document Number')),
                ('documentImage', models.ImageField(null=True, upload_to='', verbose_name='Document Image')),
                ('signature', models.ImageField(null=True, upload_to='', verbose_name='Signature')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('validUpto', models.DateTimeField(auto_now_add=True, null=True)),
                ('declaration', models.BooleanField(null=True, verbose_name='I hereby declare that the above particulars of facts and information stated are true, correct and complete to the best of my belief and knowledge')),
                ('status', models.BooleanField(default=False, null=True, verbose_name='Status')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(null=True, verbose_name='Start Date')),
                ('endDate', models.DateField(null=True, verbose_name='End Date')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainee.course')),
                ('trainee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainee.trainee')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainee.department'),
        ),
    ]
