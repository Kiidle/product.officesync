# Generated by Django 3.2.20 on 2023-11-06 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0008_signature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signature',
            old_name='corpotion',
            new_name='corporation',
        ),
    ]
