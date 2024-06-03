# Generated by Django 5.0.6 on 2024-06-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_feeding_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='finch',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]