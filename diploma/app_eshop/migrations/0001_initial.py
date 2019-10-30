# Generated by Django 2.2.4 on 2019-10-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('price', models.CharField(max_length=10, verbose_name='Price')),
                ('qty', models.CharField(max_length=10, verbose_name='Quantity')),
                ('image', models.CharField(max_length=128, verbose_name='Image')),
                ('release_date', models.DateField(verbose_name='Release date')),
                ('status', models.CharField(choices=[('available', 'Available'), ('not available', 'Not available'), ('awaiting delivery', 'Awaiting delivery')], default='available', max_length=30)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
