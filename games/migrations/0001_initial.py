# Generated by Django 4.0 on 2022-01-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='gamesrev',
            fields=[
                ('games_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=200)),
                ('noOfRev', models.IntegerField(default=1)),
                ('game_img', models.ImageField(default='', upload_to='games/images')),
            ],
        ),
        migrations.CreateModel(
            name='myrev',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('game_name', models.CharField(default='', max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
