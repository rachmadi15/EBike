# Generated by Django 3.2.9 on 2021-11-09 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=16)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
