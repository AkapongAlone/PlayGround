# Generated by Django 3.0.10 on 2021-11-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_pattern_shift_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='timeend',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pattern',
            name='timestart',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
