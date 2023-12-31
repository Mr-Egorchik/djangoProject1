# Generated by Django 4.1 on 2023-09-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0011_alter_course_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('logo_path', models.ImageField(upload_to='directors/')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('logo_path', models.ImageField(upload_to='managers/')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=20),
        ),
    ]
