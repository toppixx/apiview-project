# Generated by Django 2.0.5 on 2018-07-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0006_auto_20180506_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doornfctagmodel',
            name='door_nfc_tag',
        ),
        migrations.AddField(
            model_name='doornfctagmodel',
            name='nfc_tag',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
