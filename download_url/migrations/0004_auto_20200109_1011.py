# Generated by Django 3.0.2 on 2020-01-09 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('download_url', '0003_auto_20200109_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='download_url.Channel'),
        ),
    ]
