# Generated by Django 4.0.1 on 2022-02-01 20:47

import core.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation')),
                ('modified', models.DateField(auto_now=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-cog', 'Gear'), ('lni-laptop-phone', 'Laptop'), ('lni-leaf', 'Leaf'), ('lni-layers', 'Layers'), ('lni-rocket', 'Rocket')], max_length=18, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation')),
                ('modified', models.DateField(auto_now=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation')),
                ('modified', models.DateField(auto_now=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('service', models.CharField(max_length=100, verbose_name='Service')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-cog', 'Gear'), ('lni-stats-up', 'Graph'), ('lni-users', 'Users'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Rocket')], max_length=12, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation')),
                ('modified', models.DateField(auto_now=True, verbose_name='Updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('image', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Image')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.position', verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
