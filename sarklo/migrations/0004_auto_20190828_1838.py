# Generated by Django 2.2.3 on 2019-08-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarklo', '0003_auto_20190827_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oglas',
            name='kategorija',
            field=models.CharField(choices=[('OD', 'Odeca'), ('OB', 'Obuca'), ('KG', 'Knjige'), ('IG', 'Igracke'), ('TE', 'Tehnika'), ('RK', 'Rukotvorine')], default='KG', max_length=2),
        ),
    ]
