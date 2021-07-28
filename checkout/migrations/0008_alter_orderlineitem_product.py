# Generated by Django 3.2.3 on 2021-07-28 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_image_url'),
        ('checkout', '0007_alter_orderlineitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
