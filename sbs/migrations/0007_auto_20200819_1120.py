# Generated by Django 2.2.6 on 2020-08-19 11:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sbs', '0006_auto_20200819_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='athlete',
            options={'default_permissions': (), 'managed': False, 'ordering': ['pk']},
        ),
    ]