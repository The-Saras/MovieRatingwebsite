# Generated by Django 3.1.5 on 2021-01-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('srno', models.AutoField(primary_key=True, serialize=False)),
                ('MovName', models.CharField(max_length=60)),
                ('slug', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('story', models.TextField()),
                ('Movlanguage', models.CharField(max_length=20)),
                ('postImg', models.ImageField(default='', upload_to='movie/images')),
                ('catMov', models.TextField(max_length=50)),
                ('actors', models.TextField()),
                ('trailerUrl', models.URLField()),
            ],
        ),
    ]