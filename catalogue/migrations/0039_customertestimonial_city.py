# Generated by Django 2.2.13 on 2022-05-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0038_auto_20220519_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='customertestimonial',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='City'),
        ),
    ]
