# Generated by Django 3.1.7 on 2021-03-15 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Animals',
            new_name='Hacker',
        ),
        migrations.RenameField(
            model_name='hacker',
            old_name='ani_description',
            new_name='hacker_description',
        ),
        migrations.RenameField(
            model_name='hacker',
            old_name='ani_image',
            new_name='hacker_image',
        ),
        migrations.RenameField(
            model_name='hacker',
            old_name='ani_name',
            new_name='hacker_name',
        ),
    ]
