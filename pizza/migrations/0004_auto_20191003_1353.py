# Generated by Django 2.2.5 on 2019-10-03 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_auto_20191003_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skladnik',
            name='cena',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
