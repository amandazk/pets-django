# Generated by Django 2.2.4 on 2019-08-15 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190815_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='nome',
            new_name='user',
        ),
        migrations.AlterModelTable(
            name='pet',
            table='pet',
        ),
    ]
