# Generated by Django 2.2.2 on 2019-07-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=20)),
                ('Pwd', models.CharField(max_length=8)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('Dob', models.DateField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
