# Generated by Django 2.1.2 on 2019-03-27 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0020_auto_20190327_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics',
            old_name='save',
            new_name='Goal_save',
        ),
    ]
