# Generated by Django 3.2 on 2021-06-25 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stat',
            field=models.CharField(default='single', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.CharField(default='train-staion', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.URLField(default='https://www.google.com', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='zipCode',
            field=models.CharField(default='123asd', max_length=15),
            preserve_default=False,
        ),
    ]
