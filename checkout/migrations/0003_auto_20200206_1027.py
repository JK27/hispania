# Generated by Django 3.0.2 on 2020-02-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200205_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='order',
            name='landline',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='address1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='email_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='town',
            field=models.CharField(default='', max_length=50),
        ),
    ]
