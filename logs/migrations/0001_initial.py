# Generated by Django 4.2.13 on 2024-06-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('timestamp', models.DateTimeField()),
                ('request', models.TextField()),
                ('status', models.IntegerField()),
                ('size', models.IntegerField()),
            ],
        ),
    ]
