# Generated by Django 3.0 on 2020-01-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
