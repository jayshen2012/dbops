# Generated by Django 2.2.5 on 2019-09-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mysqlIns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='实例名')),
                ('address', models.CharField(blank=True, max_length=512, null=True, verbose_name='实例地址')),
                ('isslave', models.CharField(choices=[(0, '主库'), (1, '从库')], default=0, max_length=32, verbose_name='是否主从')),
                ('version', models.CharField(blank=True, max_length=64, null=True, verbose_name='数据库版本')),
            ],
        ),
    ]