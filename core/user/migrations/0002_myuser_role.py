# Generated by Django 5.0.2 on 2024-02-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('CUS', 'Customer'), ('REP', 'Repair Man')], default='CUS', max_length=16),
        ),
    ]
