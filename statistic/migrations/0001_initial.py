# Generated by Django 3.2.6 on 2021-09-11 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date_bday', models.DateField(db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stanok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('number', models.CharField(max_length=5, null=True)),
                ('workers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='statistic.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=20, null=True)),
                ('value', models.CharField(max_length=10, null=True)),
                ('stanok', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='statistic.stanok')),
            ],
        ),
    ]
