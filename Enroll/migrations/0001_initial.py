# Generated by Django 3.1 on 2020-09-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
