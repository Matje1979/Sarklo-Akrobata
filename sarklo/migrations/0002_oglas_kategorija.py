# Generated by Django 2.2.3 on 2019-08-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarklo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oglas',
            name='kategorija',
            field=models.CharField(default='', max_length=100),
        ),
    ]
