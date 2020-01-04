# Generated by Django 3.0.2 on 2020-01-04 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.IntegerField(blank=True, null=True)),
                ('admin_id', models.IntegerField(blank=True, null=True)),
                ('ad_user', models.CharField(blank=True, max_length=50, null=True)),
                ('chat_title', models.CharField(max_length=50)),
                ('chat_username', models.CharField(max_length=50)),
                ('message_id', models.IntegerField(blank=True, null=True)),
                ('date', models.IntegerField(blank=True, null=True)),
                ('text', models.TextField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_wholesale', models.BooleanField(default=False)),
                ('is_retail', models.BooleanField(default=False)),
                ('shoes', models.BooleanField(default=False)),
                ('bags', models.BooleanField(default=False)),
                ('women_clothes', models.BooleanField(default=False)),
                ('men_clothes', models.BooleanField(default=False)),
                ('kids_clothes', models.BooleanField(default=False)),
                ('underwear', models.BooleanField(default=False)),
                ('makeup', models.BooleanField(default=False)),
                ('homestuff', models.BooleanField(default=False)),
                ('electric_home', models.BooleanField(default=False)),
                ('glasses', models.BooleanField(default=False)),
                ('electrical', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='download_url.Button')),
            ],
        ),
    ]