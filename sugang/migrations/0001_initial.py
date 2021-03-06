# Generated by Django 3.1.1 on 2020-10-30 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='NAME')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='One Line Description')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='NAME')),
                ('number', models.TextField(max_length=30, verbose_name='NUMBER')),
                ('major', models.TextField(verbose_name='MAJOR')),
                ('upload_dt', models.DateTimeField(auto_now_add=True, verbose_name='UPDATE DATE')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sugang.subject')),
            ],
            options={
                'ordering': ('subject',),
            },
        ),
    ]
