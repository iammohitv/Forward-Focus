# Generated by Django 3.0.6 on 2020-05-10 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forward', '0005_auto_20200510_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileevaluation',
            name='AOI_3',
        ),
    ]