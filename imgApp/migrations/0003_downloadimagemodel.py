# Generated by Django 3.0.4 on 2020-03-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgApp', '0002_auto_20200325_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('preset_gray_or_poster_or_solar_or_none', models.CharField(max_length=50)),
            ],
        ),
    ]
