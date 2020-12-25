# Generated by Django 3.1.4 on 2020-12-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=250)),
                ('authorbook', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
