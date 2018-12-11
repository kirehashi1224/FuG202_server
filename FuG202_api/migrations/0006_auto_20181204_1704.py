# Generated by Django 2.0.6 on 2018-12-04 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuG202_api', '0005_delete_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistanceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenreTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PriceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='distanceTags',
            field=models.ManyToManyField(related_name='restaurants', to='FuG202_api.DistanceTag'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='genreTags',
            field=models.ManyToManyField(related_name='restaurants', to='FuG202_api.GenreTag'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='priceTags',
            field=models.ManyToManyField(related_name='restaurants', to='FuG202_api.PriceTag'),
        ),
    ]