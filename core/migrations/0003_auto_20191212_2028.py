# Generated by Django 2.2 on 2019-12-12 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190827_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=255)),
                ('date_begin_validity', models.DateTimeField(null=True)),
                ('date_end_validity', models.DateTimeField(null=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='core.App')),
            ],
        ),
        migrations.AddConstraint(
            model_name='appversion',
            constraint=models.UniqueConstraint(fields=('app', 'version'), name='unique_app_version'),
        ),
    ]
