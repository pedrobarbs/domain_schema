# Generated by Django 2.2 on 2019-06-07 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190607_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapfilter',
            name='map',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='filters', to='core.EntityMap'),
            preserve_default=False,
        ),
    ]
