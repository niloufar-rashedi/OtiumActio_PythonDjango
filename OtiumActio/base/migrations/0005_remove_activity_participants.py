# Generated by Django 4.0.2 on 2022-02-22 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_activity_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='participants',
        ),
    ]
