# Generated by Django 3.0.10 on 2021-10-27 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211026_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='machineprocess',
            new_name='machine_process',
        ),
    ]
