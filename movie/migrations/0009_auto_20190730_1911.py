# Generated by Django 2.2.3 on 2019-07-30 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20190730_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='cover',
            field=models.ImageField(blank=True, upload_to='Movie'),
        ),
    ]
