# Generated by Django 3.1.6 on 2021-02-09 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210209_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='image1',
        ),
    ]
