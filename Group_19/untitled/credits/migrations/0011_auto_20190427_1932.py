# Generated by Django 2.2 on 2019-04-27 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0010_auto_20190414_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='D69E3499AE70', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADD2AC66D062', max_length=14),
        ),
    ]
