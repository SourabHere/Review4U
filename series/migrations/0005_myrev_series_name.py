# Generated by Django 4.0 on 2022-01-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_myrev'),
    ]

    operations = [
        migrations.AddField(
            model_name='myrev',
            name='series_name',
            field=models.CharField(default='', max_length=150),
        ),
    ]
