# Generated by Django 3.2.25 on 2024-06-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]