# Generated by Django 4.0 on 2022-01-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_meal_watering_tod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=200)),
                ('effects', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['-date']},
        ),
    ]