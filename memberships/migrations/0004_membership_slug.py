# Generated by Django 3.0.3 on 2020-03-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0003_auto_20200122_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='slug',
            field=models.SlugField(default=models.CharField(default='', max_length=50)),
        ),
    ]
