# Generated by Django 2.2.5 on 2019-09-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190917_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotation',
            name='isfavorite',
            field=models.BooleanField(default=False),
        ),
    ]
