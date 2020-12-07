# Generated by Django 3.1.1 on 2020-09-23 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Namecard_TBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='NAME')),
                ('tel', models.CharField(max_length=50, verbose_name='MOBILE')),
                ('company', models.CharField(blank=True, max_length=50, verbose_name='COMPANY')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='EMAIL')),
                ('group', models.CharField(blank=True, max_length=50, verbose_name='GROUP')),
                ('create_dt', models.DateTimeField(blank=True, max_length=50, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(blank=True, max_length=50, verbose_name='MODIFY DATE')),
                ('birth_dt', models.DateTimeField(verbose_name='BIRTH DATE')),
            ],
            options={
                'ordering': ('group', 'name'),
            },
        ),
    ]
