# Generated by Django 2.2.4 on 2021-06-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0006_auto_20210605_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]