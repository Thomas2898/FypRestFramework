# Generated by Django 2.1.2 on 2019-01-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={},
        ),
        migrations.RemoveField(
            model_name='player',
            name='code',
        ),
        migrations.RemoveField(
            model_name='player',
            name='created',
        ),
        migrations.RemoveField(
            model_name='player',
            name='language',
        ),
        migrations.RemoveField(
            model_name='player',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='player',
            name='style',
        ),
        migrations.RemoveField(
            model_name='player',
            name='title',
        ),
        migrations.AddField(
            model_name='player',
            name='DOB',
            field=models.CharField(default='22/01/2019', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default='Thomas', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='teamID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]