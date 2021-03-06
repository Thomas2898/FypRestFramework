# Generated by Django 2.1.2 on 2019-03-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0017_statistics_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='Black_card',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='Goal_conceded',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='Kickout_lost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='Kickout_won',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='Red_card',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='Yellow_card',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistics',
            name='save',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
