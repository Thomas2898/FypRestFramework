# Generated by Django 2.1.2 on 2019-03-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0019_auto_20190327_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='Goal_conceded',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='save',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
