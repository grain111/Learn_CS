# Generated by Django 2.1.7 on 2019-05-14 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='p_large',
            field=models.FloatField(blank=True),
        ),
    ]
