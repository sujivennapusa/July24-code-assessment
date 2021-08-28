# Generated by Django 3.2.6 on 2021-08-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=150)),
            ],
        ),
    ]
