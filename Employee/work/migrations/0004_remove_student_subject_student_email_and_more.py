# Generated by Django 4.2.6 on 2023-11-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_employee_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subject',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='place',
            field=models.CharField(max_length=20),
        ),
    ]
