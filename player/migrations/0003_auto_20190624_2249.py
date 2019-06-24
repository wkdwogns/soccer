# Generated by Django 2.2 on 2019-06-24 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20190622_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='team',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='age',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='creDt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='height',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='position',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='speed',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='weight',
            field=models.CharField(max_length=30, null=True),
        ),
    ]