# Generated by Django 4.0.3 on 2022-04-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=64)),
                ('starting_bid', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]