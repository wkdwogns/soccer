# Generated by Django 2.2 on 2019-06-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20190430_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='creDt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
