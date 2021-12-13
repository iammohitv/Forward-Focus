# Generated by Django 3.0.6 on 2020-05-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forward', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('fees', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gre_CSEECE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('fees', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gre_MechanicalCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('fees', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
    ]