# Generated by Django 4.1.1 on 2022-10-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_functions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functions',
            name='func_value',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
