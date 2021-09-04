# Generated by Django 3.2.6 on 2021-08-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guesswork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('witch_1', models.CharField(max_length=2, verbose_name='число')),
                ('witch_2', models.CharField(max_length=2, verbose_name='число')),
            ],
        ),
        migrations.CreateModel(
            name='HiddenNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=2, verbose_name='числа')),
            ],
        ),
        migrations.CreateModel(
            name='PowerOfAttorney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attorney_1', models.CharField(max_length=3, verbose_name='доверие-1')),
                ('attorney_2', models.CharField(max_length=3, verbose_name='доверие-2')),
            ],
        ),
    ]