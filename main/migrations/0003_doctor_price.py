# Generated by Django 2.2.7 on 2019-11-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_branch_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='price',
            field=models.CharField(default='', max_length=10),
        ),
    ]
