# Generated by Django 4.0 on 2022-01-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesrev',
            name='email',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='gamesrev',
            name='desc',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
