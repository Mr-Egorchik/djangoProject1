# Generated by Django 4.1 on 2023-08-21 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_course_diagram_path_course_for_whom_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(to='mainpage.module'),
        ),
        migrations.AddField(
            model_name='course',
            name='speaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage.speaker'),
        ),
    ]