# Generated by Django 4.0.1 on 2022-01-19 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(choices=[('lni-cog', 'Gear'), ('lni-stats-up', 'Graph'), ('lni-users', 'Users'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket')], max_length=12, verbose_name='Icon'),
        ),
    ]
