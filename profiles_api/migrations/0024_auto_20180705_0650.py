# Generated by Django 2.0.5 on 2018-07-05 06:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0023_auto_20180705_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfcdoor',
            name='doorUUID',
            field=models.UUIDField(default=uuid.UUID('90baaca0-718e-4072-b511-2ecd24b5b5ad'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nfckey',
            name='AESEncryptKey',
            field=models.BinaryField(default=b'%\x81\x90\x16Q\xf8\xa9\x98\x99\xb4\xe6\x06\xd84\xd1$#\x16E\xd1\xc0\xb7\xe6\x99b.\x1bO\x166\x0f\xda#\xe4\xa9\xd7\xeb\xbbi\x98% (lz\xe07\xbb\xc0\xb7\xbb\xab\x8a\x89J\x956\x11\x10M\xb0\xac\x80\xdf\xd8Y\x11\x94\x9b&\x1e\x0bf\xe4\x98\xfc\xf0\x96\xc5\xde-V\xc5f\xd1\xdb\xc6\xf7[u\xb9\xedD\xf8\xfb\x7f\xa9\n"\xea\xea\xdd5\'\x87\xbe\xba\xaa:\xd3\xc2\xebAk\xbc\xdd.\'\xcd\x99\xd7\xafw_\x00\xe48"', max_length=128),
        ),
        migrations.AlterField(
            model_name='nfckey',
            name='keyUUID',
            field=models.UUIDField(default=uuid.UUID('fb9ed9a3-596d-4814-bcf4-7502125827bf'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='TDAT',
            field=models.TextField(default='v0f0tUBaYYZ1kWRgep65mzzzSRUqzVn2jEnWu8VkRNzLFBFZ7Ml9Clf0bjaoLidF1J17oWAMQ0ziC8dvJYRcIPxIbCtFZ6dGMlGkHU473qJ0MW6n7V2cIV8wDZzaFfInpr6Wyi7PG5EcMEehXtJ8OoJuJzeh6iZcovnGBJMyBAelG6TEKVh0hpOi8WFHal3P3KIOz8YrTRlxAvtBmOoOWmVXsDNa8d5z1bFAloqpWtRCb9BZFbcXuwPFl9EBjI1a', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='accesingUDID',
            field=models.TextField(default='14iWHlA6fqhD8EGshqIEdn4ASIYEao0oPCXLiT6OEyabUteLx5OC6OuskT9HY40nnyPlbGNbkCNW1jzvmK3bIDQZCHVm2IXLUiwvBSfmbjoaTL3usJn9Ncp5AUOVRQUiQf5bxhLCHjKxUOWsXvqarc2XlWbzcNSIadcdN0GSM2rXuquB5t2nA4ZB08PPMMJFHP9CmEzwCXMkiQvk3Hd8Il1vb018OgolfEMZrl9jvApZgx7MMfBq6hKUXlSqNNSf', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='encryptionKey',
            field=models.TextField(default='BGSxxsoGsCxrjhFeXVACwtCezfMMOt9BHQfxg11drBTfHR6JKhpDqwfibdVLg6jbAzVV7I9uUgXJtNC8d8PwbNKLVSgBh7t3M6xUwir9n8vshD0VC6juWahzyiVBpJsA6uTvRdrLGfmMQBnhP6jdBkwRHpS7tOipq2Mny2zmIPIabJRpLC7XBc3nzK4qehs4j0ia8gI3HwArQFSTytl3mEJ3qAexCMw7BVt840Q34QkxUNIi3aqtm8QmaDhj0UF1', editable=False, max_length=256),
        ),
    ]
