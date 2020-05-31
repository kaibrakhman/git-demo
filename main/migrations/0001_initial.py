# Generated by Django 2.2.7 on 2019-11-25 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_t', models.CharField(default='', max_length=10)),
                ('finish_t', models.CharField(default='', max_length=10)),
                ('start_l', models.CharField(default='', max_length=10)),
                ('finish_l', models.CharField(default='', max_length=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='main.Branch')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='main.Days')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=100)),
                ('rank', models.TextField()),
                ('description', models.TextField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Branch')),
            ],
        ),
    ]
