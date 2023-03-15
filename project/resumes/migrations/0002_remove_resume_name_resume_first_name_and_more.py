# Generated by Django 4.1.7 on 2023-03-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='name',
        ),
        migrations.AddField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default='Иван', max_length=256),
        ),
        migrations.AddField(
            model_name='resume',
            name='last_name',
            field=models.CharField(default='Иванов', max_length=256),
        ),
    ]