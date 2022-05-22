# Generated by Django 3.2.8 on 2021-11-08 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ncity', models.CharField(max_length=100)),
                ('nhead', models.CharField(max_length=1000)),
                ('nsubject', models.CharField(max_length=200)),
                ('ndes', models.TextField(max_length=5000)),
                ('ndate', models.DateField()),
                ('npic', models.ImageField(default='', upload_to='static/news/')),
                ('ncategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
    ]
