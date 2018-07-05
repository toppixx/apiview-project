# Generated by Django 2.0.5 on 2018-07-05 06:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0020_auto_20180705_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfcdoor',
            name='doorUUID',
            field=models.UUIDField(default=uuid.UUID('85249385-1e66-4778-bbd5-1a1968bba29a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nfckey',
            name='AESEncryptKey',
            field=models.BinaryField(default=b'L\x13\xc0\'\x1e\x03\xcc\x1c\xd4=\xa0\x91\xaa,\x91\x17\xfaY\x04f\x82\x85\xe2\xf6\xbd\x8d\xb5x\xe4"\xd8\nT\xb7\x886(\x8d\xb8a\x11U\xfd,n\x05\xa9\x99m\xa0\xa5\r\xb7\xb0?T \xf1:y\xc8\xc0\xd3\xed\xb0[\x9cx\x85\x01g\x88Y\xf7\xc2\xee\x9c\x11\xa1\x87\xfb\xe1\xc3b\xccZa?F\xfc\x91\r\x1e\xca\xda\x01\xc7.\xa0\xeb\x8f\x9f\x1f\xe7=?\xb5{\x7f\xcf\x98\xfbo2\t5"\xff\xe2\x9a\xf4G\xd6\\\xc1-\xed;', max_length=128),
        ),
        migrations.AlterField(
            model_name='nfckey',
            name='keyUUID',
            field=models.UUIDField(default=uuid.UUID('aceb4f72-0e05-47c3-bb64-16a45d66cfa1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='TDAT',
            field=models.TextField(default='hUPVwj7W8ATcakgbP2YH8WO3Vc6rAMPAXP9jskkKy0JDGPQp9IWrMY9ovLR7ghpQdtFe0U9jjJGnf0o1JxP1PnFPyh0pt32wiPbLFuaVIX1dVaL0g5xljzOB5VYcru1cQrzi1jNDjd6Hi5Zhf83H2300ry967olvN8QPCQUzAHELyEn8xYcv9xFICPiB4ARgmoZXaK4ij2DPQyOW5GhAWfsh3Z9iuVJGBh6hkjUFymDqh0E6CxyHq9QJkgrWcDEf', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='accesingUDID',
            field=models.TextField(default='1iUmQS5VrTX7m4u1cpMVAeJfEArJbl78nShDJliNztn4pIlQwgU6atmK7ZaydprJN2jRu1hsXtFcgujWCGSb83kx0woxJWeuP6aeyNzUBaBpaQykWkfshKEuZS2Ae4unKttpJxheK6gj6nUAWlNuzV2Fz9N2KgZaFlKlnYCzHwfDIf6R2rfDkCZdSF2JDLnBY9eBa5kPxuC5Ah63Izx8zwq9Cnb4WNVbem28JOrR8BiiUJpanQN4QNSlnFRCXtRY', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='encryptionKey',
            field=models.TextField(default='jIz4wSNUHBzlXF1KDAWs8qljR9pW99FmzkxFQBSS0p9Sj9tSitsdqw0HpSHvq7eJx4w9OY8rEEd2xPRCING7rMVq9Udpl5oJZOmtfbzdyvJtzuuv3ZsB5xjMIJrY0nNr8dYMYn6vUwgR1O0iRLCkAvgqmnPZmnRwOmFGFNWRJHRA5NpZkplxoQA5LiGIve1ebzm33wza39qaVXONHGbGmYEnSnZmt7WqHZpf3UnEIGIBn6YDqpl32210qllvzoHQ', editable=False, max_length=256),
        ),
    ]
