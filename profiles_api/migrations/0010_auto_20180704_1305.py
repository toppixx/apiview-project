# Generated by Django 2.0.5 on 2018-07-04 13:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0009_auto_20180704_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfclistofdoors',
            name='listOfDoors',
            field=models.ManyToManyField(to='profiles_api.NfcDoor'),
        ),
        migrations.AlterField(
            model_name='nfckey',
            name='keyUUID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
