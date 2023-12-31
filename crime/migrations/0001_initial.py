# Generated by Django 3.2.3 on 2023-07-27 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, default=1, null=True)),
                ('month', models.IntegerField(blank=True, default=1, null=True)),
                ('day', models.IntegerField(blank=True, default=1, null=True)),
                ('hour', models.IntegerField(blank=True, default=1, null=True)),
                ('minute', models.IntegerField(blank=True, default=1, null=True)),
                ('block', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('neighbor', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('x', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('y', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
        ),
    ]
