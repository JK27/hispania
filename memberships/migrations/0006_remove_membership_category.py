# Generated by Django 3.0.3 on 2020-04-06 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0005_membership_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='category',
        ),
    ]
