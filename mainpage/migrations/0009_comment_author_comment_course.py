# Generated by Django 4.1 on 2023-09-05 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_remove_course_for_whom_1_remove_course_for_whom_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainpage.course'),
        ),
    ]
