# Generated by Django 2.2.13 on 2022-11-24 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20181115_1953'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommunicationEventType',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]