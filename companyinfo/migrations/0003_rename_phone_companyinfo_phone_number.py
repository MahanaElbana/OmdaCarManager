# Generated by Django 4.2.4 on 2024-01-19 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0002_alter_companyinfo_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinfo',
            old_name='phone',
            new_name='phone_number',
        ),
    ]