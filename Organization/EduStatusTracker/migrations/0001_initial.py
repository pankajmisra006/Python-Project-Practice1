# Generated by Django 3.1 on 2020-08-12 11:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization_authorization',
            fields=[
                ('orgAuthorizationId', models.IntegerField(primary_key=True, serialize=False)),
                ('authorizationType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization_security_question',
            fields=[
                ('orgSecurityQueID', models.IntegerField(primary_key=True, serialize=False)),
                ('securityQuestionID', models.CharField(max_length=100)),
                ('securityQuestion', models.CharField(max_length=100)),
                ('securityAnswers', models.CharField(max_length=100)),
                ('lastModifiedDate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orgnization_user_verification',
            fields=[
                ('registrationID', models.IntegerField(primary_key=True, serialize=False)),
                ('oneTimePassword', models.CharField(max_length=100)),
                ('boardType', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_FTL', models.IntegerField(default=0)),
                ('password_exp_flag', models.BooleanField(default=True)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('lastModifiedDate', models.DateField(auto_now_add=True)),
                ('securityQuestionID', models.CharField(default=uuid.uuid4, max_length=100, unique=True)),
            ],
        ),
    ]