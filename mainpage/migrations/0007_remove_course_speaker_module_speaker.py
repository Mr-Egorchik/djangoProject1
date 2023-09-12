# Generated by Django 4.1 on 2023-08-21 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_course_modules_course_speaker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='speaker',
        ),
        migrations.AddField(
            model_name='module',
            name='speaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage.speaker'),
        ),
    ]
