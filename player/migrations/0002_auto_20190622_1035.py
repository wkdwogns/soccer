# Generated by Django 2.2 on 2019-06-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='age',
            field=models.CharField(max_length=10),
        ),
    ]