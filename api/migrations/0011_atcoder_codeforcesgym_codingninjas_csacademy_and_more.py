# Generated by Django 4.2.1 on 2023-06-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_codeforces_delete_company_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtCoder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CodeForcesGym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CodingNinjas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CSAcademy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Geekforgeeks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='HackerEarth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='HackerRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TopCoder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('duration', models.IntegerField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=255)),
                ('in_24_hours', models.BooleanField()),
            ],
        ),
    ]
