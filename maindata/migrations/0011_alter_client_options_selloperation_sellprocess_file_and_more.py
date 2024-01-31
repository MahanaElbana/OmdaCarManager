# Generated by Django 4.2.4 on 2024-01-17 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindata', '0010_car_color_remove_pill_client_remove_product_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': '   عميل', 'verbose_name_plural': '  العميل '},
        ),
        migrations.AddField(
            model_name='selloperation',
            name='sellprocess_file',
            field=models.FileField(blank=True, null=True, upload_to='sellprocess_files/', verbose_name=' ملف'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gawap_type',
            field=models.CharField(blank=True, choices=[('1', 'بصرى'), ('2', ' سمعى'), ('2', ' ذهنى'), ('2', ' حركى')], default='1', max_length=200, null=True, verbose_name='  نوع الجواب '),
        ),
        migrations.AlterField(
            model_name='selloperation',
            name='sell_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 17, 22, 6, 25, 874521), null=True, verbose_name=' تاريخ الخروج'),
        ),
    ]