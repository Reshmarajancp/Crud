# Generated by Django 4.2.6 on 2023-12-04 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_stud_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]