# Generated by Django 4.2.1 on 2023-05-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_user_usercreate'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreate',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
