# Generated by Django 2.2.4 on 2021-06-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_auto_20210602_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='No description'),
            preserve_default=False,
        ),
    ]
