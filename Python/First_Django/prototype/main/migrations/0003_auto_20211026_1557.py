# Generated by Django 3.0.10 on 2021-10-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_pattern_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='cstart',
            field=models.IntegerField(blank=True, db_column='Cstart', null=True),
        ),
        migrations.AddField(
            model_name='model',
            name='rstart',
            field=models.IntegerField(blank=True, db_column='Rstart', null=True),
        ),
    ]
