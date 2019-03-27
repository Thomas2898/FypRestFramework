# Generated by Django 2.1.2 on 2019-03-26 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20190326_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pass', models.IntegerField()),
                ('Pass_Miss', models.IntegerField()),
                ('Point', models.IntegerField()),
                ('Point_Miss', models.IntegerField()),
                ('Goal', models.IntegerField()),
                ('Goal_Miss', models.IntegerField()),
                ('Fixture_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Fixture')),
                ('Player_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Player')),
            ],
        ),
        migrations.RemoveField(
            model_name='stats',
            name='Fixtures',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='PlayerID',
        ),
        migrations.DeleteModel(
            name='Stats',
        ),
    ]
