# Generated by Django 4.1 on 2023-08-06 15:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_alter_course_id_alter_direction_id_alter_module_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=127)),
                ('text', models.TextField()),
                ('img', models.ImageField(upload_to='speakers/')),
            ],
        ),
    ]
