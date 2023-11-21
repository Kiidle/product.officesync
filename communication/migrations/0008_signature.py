# Generated by Django 3.2.20 on 2023-11-06 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0007_alter_announcement_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpotion', models.CharField(default='OfficeSync', max_length=50, verbose_name='Unternehmen')),
                ('logo', models.ImageField(blank=True, default='authentication/static/images/uploads/logo_default/officesync.png', null=True, upload_to='authentication/static/images/uploads/signature', verbose_name='Logo')),
                ('country', models.CharField(default='Schweiz', max_length=50, verbose_name='Land')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='Standort')),
                ('street', models.CharField(blank=True, max_length=50, null=True, verbose_name='Strasse')),
                ('housenumber', models.CharField(blank=True, max_length=50, null=True, verbose_name='Hausnummer')),
            ],
        ),
    ]