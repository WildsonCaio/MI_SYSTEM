# Generated by Django 4.1.3 on 2022-11-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
