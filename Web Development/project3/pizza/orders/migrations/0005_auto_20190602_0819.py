# Generated by Django 2.1.7 on 2019-06-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("orders", "0004_auto_20190602_0813")]

    operations = [
        migrations.RemoveField(model_name="menuitemchoice", name="extras"),
        migrations.AddField(
            model_name="menuitemchoice",
            name="extras",
            field=models.ManyToManyField(to="orders.ExtraIngridient"),
        ),
    ]