# Generated by Django 3.1.1 on 2020-10-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='major',
            field=models.CharField(max_length=20, verbose_name='MAJOR'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='name',
            field=models.CharField(max_length=20, verbose_name='NAME'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='number',
            field=models.CharField(max_length=20, verbose_name='NUMBER'),
        ),
    ]
