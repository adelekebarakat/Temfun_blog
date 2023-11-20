# Generated by Django 4.2.7 on 2023-11-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=225),
        ),
    ]
