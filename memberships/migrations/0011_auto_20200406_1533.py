# Generated by Django 3.0.3 on 2020-04-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0010_auto_20200406_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
