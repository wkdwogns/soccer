# Generated by Django 2.2 on 2019-07-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20190602_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='creId',
            field=models.IntegerField(null=True),
        ),
    ]
