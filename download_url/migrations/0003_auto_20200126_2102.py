# Generated by Django 3.0.2 on 2020-01-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download_url', '0002_auto_20200125_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
