# Generated by Django 5.0 on 2023-12-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=225)),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('period', models.CharField(max_length=225)),
                ('technologies', models.ManyToManyField(to='experience.technology')),
            ],
        ),
    ]
