# Generated by Django 2.2.4 on 2021-06-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0007_auto_20210605_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]
