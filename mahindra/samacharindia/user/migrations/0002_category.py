# Generated by Django 3.2.8 on 2021-11-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=120)),
                ('cpic', models.ImageField(default='', upload_to='static/category/')),
                ('cdate', models.DateField()),
            ],
        ),
    ]
