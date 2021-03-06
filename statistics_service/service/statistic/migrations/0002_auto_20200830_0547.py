# Generated by Django 3.1 on 2020-08-30 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubsLog',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('time', models.TextField()),
                ('method', models.TextField()),
                ('url', models.TextField()),
                ('client', models.TextField()),
                ('client_id', models.TextField()),
                ('params', models.TextField()),
                ('headers', models.TextField()),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'clubss_stat',
            },
        ),
        migrations.CreateModel(
            name='CompetitionsLog',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('time', models.TextField()),
                ('method', models.TextField()),
                ('url', models.TextField()),
                ('client', models.TextField()),
                ('client_id', models.TextField()),
                ('params', models.TextField()),
                ('headers', models.TextField()),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'competitions_stat',
            },
        ),
        migrations.DeleteModel(
            name='DancersErrorLog',
        ),
        migrations.AlterField(
            model_name='dancerslog',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
