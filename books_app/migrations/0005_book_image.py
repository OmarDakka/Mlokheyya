# Generated by Django 2.2.4 on 2021-06-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0004_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]