# Generated by Django 4.1 on 2023-02-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default='init', max_length=10),
        ),
    ]
