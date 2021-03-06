# Generated by Django 2.2.4 on 2019-08-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IphoneSE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.TextField()),
                ('name', models.TextField()),
                ('size', models.TextField()),
                ('os', models.TextField()),
                ('ram', models.TextField()),
                ('color', models.TextField()),
                ('accum', models.TextField()),
                ('cam_dpi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.TextField()),
                ('name', models.TextField()),
                ('size', models.TextField()),
                ('os', models.TextField()),
                ('ram', models.TextField()),
                ('color', models.TextField()),
                ('accum', models.TextField()),
                ('cam_dpi', models.TextField()),
            ],
        ),
    ]
