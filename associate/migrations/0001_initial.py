# Generated by Django 3.1.7 on 2021-05-10 11:02

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
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service', models.CharField(choices=[('Education', 'Education'), ('Computer', 'Computer'), ('Tailoring', 'Tailoring'), ('Reuse Bank', 'Reuse Bank'), ('Online Service', 'Online Service'), ('Scrap', 'Scrap'), ('Other', 'Other')], max_length=255, null=True, verbose_name='Service')),
                ('uniqueID', models.CharField(default='9D527', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('firstName', models.CharField(max_length=255, null=True, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=255, null=True, verbose_name='Last Name')),
                ('mobileNumber', models.CharField(max_length=13, null=True, verbose_name='Mobile Number')),
                ('emailID', models.EmailField(max_length=254, null=True, verbose_name='Email Address')),
                ('address', models.CharField(max_length=512, null=True, verbose_name='Address')),
                ('area', models.CharField(max_length=255, null=True, verbose_name='Area')),
                ('locality', models.CharField(max_length=255, null=True, verbose_name='Locality')),
                ('district', models.CharField(max_length=255, null=True, verbose_name='District')),
                ('state', models.CharField(max_length=255, null=True, verbose_name='State')),
                ('pincode', models.CharField(max_length=255, null=True, verbose_name='Pincode')),
                ('mode', models.CharField(choices=[('Cash', 'Cash'), ('RTGs', 'RTGs'), ('Cheque', 'Cheque'), ('Paytm', 'Paytm'), ('Google Pay', 'Google Pay'), ('Phone Pe', 'Phone Pe')], max_length=255, null=True, verbose_name='Mode of Payment')),
                ('amount', models.IntegerField(null=True, verbose_name='Amount')),
                ('PANNo', models.CharField(max_length=15, null=True, verbose_name='PAN Number')),
                ('AadhaarNo', models.CharField(max_length=15, null=True, verbose_name='Aadhaar Number')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('uniqueID', models.CharField(default='D8AB7', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('firstName', models.CharField(max_length=255, null=True, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=255, null=True, verbose_name='Last Name')),
                ('mobileNumber', models.CharField(max_length=13, null=True, verbose_name='Mobile Number')),
                ('emailID', models.EmailField(max_length=254, null=True, verbose_name='Email Address')),
                ('address', models.CharField(max_length=512, null=True, verbose_name='Address')),
                ('area', models.CharField(max_length=255, null=True, verbose_name='Area')),
                ('locality', models.CharField(max_length=255, null=True, verbose_name='Locality')),
                ('district', models.CharField(max_length=255, null=True, verbose_name='District')),
                ('state', models.CharField(max_length=255, null=True, verbose_name='State')),
                ('pincode', models.CharField(max_length=255, null=True, verbose_name='Pincode')),
                ('mode', models.CharField(choices=[('Cash', 'Cash'), ('RTGs', 'RTGs'), ('Cheque', 'Cheque'), ('Paytm', 'Paytm'), ('Google Pay', 'Google Pay'), ('Phone Pe', 'Phone Pe')], max_length=255, null=True, verbose_name='Mode of Payment')),
                ('amount', models.IntegerField(null=True, verbose_name='Amount')),
                ('PANNo', models.CharField(max_length=15, null=True, verbose_name='PAN Number')),
                ('AadhaarNo', models.CharField(max_length=15, null=True, verbose_name='Aadhaar Number')),
                ('purpose', models.CharField(choices=[('Donation', 'Donation'), ('Education', 'Education'), ('Differently Abled', 'Differently Abled'), ('Medical Aid', 'Medical Aid'), ('Ration Support', 'Ration Support'), ('Women Empowerment', 'Women Empowerment'), ('Skill Development', 'Skill Development')], max_length=255, null=True, verbose_name='Purpose')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('uniqueID', models.CharField(default='7ED91', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('payeeName', models.CharField(max_length=255, null=True, verbose_name='Payee Name')),
                ('mobileNumber', models.CharField(max_length=13, null=True, verbose_name='Mobile Number')),
                ('mode', models.CharField(choices=[('Cash', 'Cash'), ('RTGs', 'RTGs'), ('Cheque', 'Cheque'), ('Paytm', 'Paytm'), ('Google Pay', 'Google Pay'), ('Phone Pe', 'Phone Pe')], max_length=255, null=True, verbose_name='Mode of Payment')),
                ('amount', models.IntegerField(null=True, verbose_name='Amount')),
                ('PANNo', models.CharField(max_length=15, null=True, verbose_name='PAN Number')),
                ('AadhaarNo', models.CharField(max_length=15, null=True, verbose_name='PAN Number')),
                ('budgetHead', models.CharField(choices=[('Salary', 'Salary'), ('Honorarium/Insentive', 'Honorarium/Insentive'), ('Consultation Charge', 'Consultation Charge'), ('Capital/Infrastructure', 'Capital/Infrastructure'), ('Printing & Stationary', 'Printing & Stationary'), ('Gadgets', 'Gadgets'), ('Staff Welfare', 'Staff Welfare'), ('Ration', 'Ration'), ('Local Conveyance', 'Local Conveyance'), ('Petrol/Vehicle Maintenance', 'Petrol/Vehicle Maintenance'), ('Service/Labour Charge', 'Service/Labour Charge')], max_length=255, null=True, verbose_name='Purpose')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='associate.project')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('uniqueID', models.CharField(default='38179', editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('profilePicture', models.ImageField(null=True, upload_to='')),
                ('firstName', models.CharField(max_length=255, null=True, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=255, null=True, verbose_name='Last Name')),
                ('fatherName', models.CharField(max_length=255, null=True, verbose_name="Father's Name")),
                ('motherName', models.CharField(max_length=255, null=True, verbose_name="Mother's Name")),
                ('dateOfBirth', models.DateField(null=True, verbose_name='Date of Birth')),
                ('age', models.IntegerField(null=True, verbose_name='Age of Candidate')),
                ('martialStatus', models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Single', 'Single'), ('Widow', 'Widow')], max_length=255, null=True, verbose_name='Martial Status')),
                ('category', models.CharField(choices=[('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('EWS', 'EWS')], max_length=255, null=True, verbose_name='Category')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=255, null=True, verbose_name='Gender')),
                ('religion', models.CharField(choices=[('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Sikh', 'Sikh'), ('Isai', 'Isai'), ('Jain', 'Jain'), ('Other', 'Other')], max_length=255, null=True, verbose_name='Religion')),
                ('mobileNumber', models.CharField(max_length=13, null=True, verbose_name='Mobile Number')),
                ('emailID', models.EmailField(max_length=254, null=True, verbose_name='Email Address')),
                ('emergencyContact', models.CharField(max_length=13, null=True, verbose_name='Emergency Contact Number')),
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
                ('signature', models.ImageField(null=True, upload_to='')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]