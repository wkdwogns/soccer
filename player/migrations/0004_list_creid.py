# Generated by Django 2.2 on 2019-07-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_auto_20190624_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='creId',
            field=models.IntegerField(null=True),
        ),
    ]