# Generated by Django 3.0 on 2021-04-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usrrg',
            name='age',
            field=models.IntegerField(default=10),
        ),
    ]
