# Generated by Django 3.0.6 on 2023-10-01 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
