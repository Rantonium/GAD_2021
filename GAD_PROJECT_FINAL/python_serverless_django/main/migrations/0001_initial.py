# Generated by Django 3.2.6 on 2021-08-04 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('file_extension', models.CharField(max_length=10)),
                ('file_type', models.CharField(max_length=255)),
                ('fileList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.filelist')),
            ],
        ),
    ]
