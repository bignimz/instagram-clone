# Generated by Django 3.1 on 2022-06-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0006_auto_20220211_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pciture'),
        ),
    ]
