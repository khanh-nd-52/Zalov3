# Generated by Django 2.2.17 on 2021-12-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='posts/%Y/%m'),
        ),
    ]
