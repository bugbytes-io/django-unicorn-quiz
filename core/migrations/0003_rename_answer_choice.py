# Generated by Django 3.2.3 on 2021-07-30 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210730_1222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Choice',
        ),
    ]
