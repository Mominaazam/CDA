# Generated by Django 3.2.7 on 2024-05-02 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ADapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internal_user',
            old_name='Password',
            new_name='HashPassword',
        ),
    ]
