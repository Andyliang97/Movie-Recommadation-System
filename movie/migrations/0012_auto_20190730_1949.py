# Generated by Django 2.2.3 on 2019-07-30 23:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0011_auto_20190730_1946'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieInfo',
            new_name='MovieReview',
        ),
    ]
