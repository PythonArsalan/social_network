# Generated by Django 3.2.7 on 2022-01-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MGN', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messageorder',
            old_name='total_follower',
            new_name='total_message',
        ),
    ]
