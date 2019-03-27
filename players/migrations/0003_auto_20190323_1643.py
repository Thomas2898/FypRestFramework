# Generated by Django 2.1.2 on 2019-03-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20190122_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='teamID',
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='players.Player'),
        ),
    ]
