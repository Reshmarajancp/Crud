# Generated by Django 4.2.6 on 2023-11-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
                ('place', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
