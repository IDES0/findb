# Generated by Django 4.2.14 on 2024-08-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holding',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
