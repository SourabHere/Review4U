# Generated by Django 4.0 on 2022-01-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_seriesrev_noofrev'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=25)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
