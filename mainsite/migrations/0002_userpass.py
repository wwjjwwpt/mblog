# Generated by Django 2.2.4 on 2019-08-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
