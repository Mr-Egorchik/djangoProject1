# Generated by Django 4.1 on 2023-09-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_remove_application_mail_application_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=15),
        ),
    ]
