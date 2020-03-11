# Generated by Django 3.0.2 on 2020-03-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20200219_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='landline',
            field=models.IntegerField(blank=True, default='', verbose_name='Home phone number (Optional)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.IntegerField(default='', verbose_name='Mobile number'),
        ),
    ]