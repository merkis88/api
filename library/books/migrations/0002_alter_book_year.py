# Generated by Django 5.1.4 on 2024-12-19 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]