# Generated by Django 4.0.1 on 2022-01-19 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_service_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='descripton',
            new_name='description',
        ),
    ]
