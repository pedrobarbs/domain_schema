# Generated by Django 2.2 on 2019-06-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190613_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='precision',
            field=models.IntegerField(null=True),
        ),
    ]
