# Generated by Django 3.0.5 on 2020-04-27 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200426_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='datecomepleted',
            new_name='datecompleted',
        ),
    ]
