# Generated by Django 2.2.28 on 2022-11-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addressgxdzjgeeam'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressgxdzjgeeam',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
