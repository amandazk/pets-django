# Generated by Django 3.1.5 on 2021-01-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190815_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='imagem',
            field=models.ImageField(upload_to='pet'),
        ),
    ]
