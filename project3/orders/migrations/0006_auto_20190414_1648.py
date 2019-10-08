# Generated by Django 2.2 on 2019-04-14 16:48

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190411_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='menu',
            name='custom',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Cart'),
        ),
    ]