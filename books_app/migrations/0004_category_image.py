# Generated by Django 2.2.4 on 2021-06-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0003_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
