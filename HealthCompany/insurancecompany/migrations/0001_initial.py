# Generated by Django 3.2 on 2021-04-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('insurance_company_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=150)),
                ('details', models.TextField()),
            ],
        ),
    ]
