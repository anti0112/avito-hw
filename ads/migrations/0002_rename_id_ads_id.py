# Generated by Django 3.2.15 on 2022-08-22 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='id',
            new_name='Id',
        ),
    ]