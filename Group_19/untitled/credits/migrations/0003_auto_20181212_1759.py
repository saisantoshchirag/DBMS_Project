# Generated by Django 2.1.1 on 2018-12-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0002_auto_20181212_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='EA2B22A1BF22', max_length=14),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='ADD31A01657E', max_length=14),
        ),
    ]
