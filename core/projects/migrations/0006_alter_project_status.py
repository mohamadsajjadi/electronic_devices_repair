# Generated by Django 4.2.7 on 2024-02-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('In Process', 'in_process'), ('Taken', 'taken'), ('Waiting', 'waiting'), ('Archive', 'archive'), ('Done', 'done')], default='Waiting', max_length=64),
        ),
    ]
