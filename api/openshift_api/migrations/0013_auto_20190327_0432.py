# Generated by Django 2.1.2 on 2019-03-27 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0012_auto_20190321_0319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='host',
            options={'ordering': ('-name',)},
        ),
    ]