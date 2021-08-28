# Generated by Django 3.2.6 on 2021-08-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarian_code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('emailid', models.CharField(max_length=50)),
            ],
        ),
    ]
