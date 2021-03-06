# Generated by Django 4.0 on 2022-01-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0002_addrev'),
    ]

    operations = [
        migrations.CreateModel(
            name='myrev',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('anime_name', models.CharField(default='', max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='addrev',
            new_name='animesrev',
        ),
    ]
