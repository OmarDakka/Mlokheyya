# Generated by Django 2.2.4 on 2021-06-05 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_merge_20210605_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default1.jpg', upload_to='images/'),
        ),
    ]