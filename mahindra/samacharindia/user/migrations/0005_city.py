# Generated by Django 3.2.8 on 2021-11-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_notification_slider_videonews'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=300)),
                ('cdate', models.DateField()),
            ],
        ),
    ]
