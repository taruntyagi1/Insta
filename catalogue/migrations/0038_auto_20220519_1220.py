# Generated by Django 2.2.13 on 2022-05-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0037_dietitionsandnutritionists_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietitionsandnutritionists',
            name='dietitions_and_nutritionists',
            field=models.CharField(choices=[('Dietitions', 'Dietitions'), ('Follower', 'Follower')], max_length=30, verbose_name='Dietitions And Nutritionists'),
        ),
    ]
