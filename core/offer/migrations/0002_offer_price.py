# Generated by Django 4.2.7 on 2024-02-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='price',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
