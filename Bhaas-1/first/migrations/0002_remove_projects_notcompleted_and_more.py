# Generated by Django 4.1.1 on 2022-09-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='notcompleted',
        ),
        migrations.AlterField(
            model_name='projects',
            name='completed',
            field=models.BooleanField(default=True),
        ),
    ]
