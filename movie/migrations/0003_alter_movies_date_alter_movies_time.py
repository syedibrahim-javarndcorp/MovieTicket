# Generated by Django 4.0 on 2021-12-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movies_date_alter_movies_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
