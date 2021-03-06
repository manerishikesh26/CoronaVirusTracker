# Generated by Django 3.0.3 on 2020-03-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid19_tb',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('Country', models.CharField(max_length=30)),
                ('total_cases', models.IntegerField(max_length=30)),
                ('today_cases', models.IntegerField(max_length=30)),
                ('total_deaths', models.IntegerField(max_length=30)),
                ('today_deaths', models.IntegerField(max_length=30)),
                ('recovered', models.IntegerField(max_length=30)),
                ('active', models.IntegerField(max_length=30)),
                ('critical', models.IntegerField(max_length=30)),
            ],
        ),
    ]
