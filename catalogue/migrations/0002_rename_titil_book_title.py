# Generated by Django 3.2.2 on 2021-05-07 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='titil',
            new_name='title',
        ),
    ]
