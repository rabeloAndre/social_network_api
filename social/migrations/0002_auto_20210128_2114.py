# Generated by Django 3.1 on 2021-01-29 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=270),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=270),
        ),
    ]