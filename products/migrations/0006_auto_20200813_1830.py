# Generated by Django 3.0.7 on 2020-08-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200805_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumper',
            name='Phone_Number',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
