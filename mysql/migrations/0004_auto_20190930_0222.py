# Generated by Django 2.2.5 on 2019-09-30 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql', '0003_confirmstring_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysqlins',
            name='pwd',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='密码 '),
        ),
        migrations.AddField(
            model_name='mysqlins',
            name='user',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='用户'),
        ),
    ]