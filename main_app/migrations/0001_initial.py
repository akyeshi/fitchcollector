# Generated by Django 5.0.6 on 2024-05-29 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('habitat', models.CharField(max_length=100)),
                ('diet', models.CharField(max_length=100)),
                ('conservation_status', models.CharField(max_length=100)),
            ],
        ),
    ]
