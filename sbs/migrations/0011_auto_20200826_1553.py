# Generated by Django 2.2.6 on 2020-08-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sbs', '0010_auto_20200826_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preregistration',
            name='kademe_definition',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]