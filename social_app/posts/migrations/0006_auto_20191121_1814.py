# Generated by Django 2.2.7 on 2019-11-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_auto_20191121_0115"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment", name="text", field=models.CharField(max_length=150),
        ),
    ]
