# Generated by Django 3.2.9 on 2021-11-09 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregestration',
            old_name='firsName',
            new_name='firstName',
        ),
    ]
