# Generated by Django 4.2.7 on 2023-11-07 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_post_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
