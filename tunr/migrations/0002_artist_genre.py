# Generated by Django 4.0.5 on 2022-06-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.CharField(default='rock', max_length=20),
        ),
    ]