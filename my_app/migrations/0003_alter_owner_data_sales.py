# Generated by Django 3.2 on 2022-08-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_owner_data_sales'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='data_sales',
            field=models.DateTimeField(),
        ),
    ]
