# Generated by Django 3.0.4 on 2020-03-25 01:53

from django.db import migrations, models
import imgApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('preset', models.CharField(max_length=50)),
                ('Main_Img', models.FileField(upload_to=imgApp.models.content_file_name)),
            ],
        ),
    ]
