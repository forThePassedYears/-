# Generated by Django 2.0.6 on 2019-05-13 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20190513_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='demo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]