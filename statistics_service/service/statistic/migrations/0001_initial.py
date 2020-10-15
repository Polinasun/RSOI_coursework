# Generated by Django 3.1 on 2020-08-29 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DancersErrorLog',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('time', models.TextField()),
                ('error', models.TextField()),
                ('method', models.TextField()),
                ('url', models.TextField()),
                ('params', models.TextField()),
                ('headers', models.TextField()),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'dancers_error_stat',
            },
        ),
        migrations.CreateModel(
            name='DancersLog',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
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
                'db_table': 'dancers_stat',
            },
        ),
    ]
