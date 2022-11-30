# Generated by Django 2.2.13 on 2022-10-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0067_auto_20220929_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='show_in_subscription_plan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='subscription_ordering',
            field=models.IntegerField(default=0),
        ),
    ]