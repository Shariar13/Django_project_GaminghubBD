# Generated by Django 3.1.2 on 2021-07-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210701_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='pubg_registered_id_10_taka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('tournament_name', models.CharField(max_length=100, null=True)),
                ('pubg_id', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('transactionid', models.CharField(max_length=100)),
                ('phone_4_digit', models.CharField(max_length=100)),
            ],
        ),
    ]
