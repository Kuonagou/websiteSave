# Generated by Django 4.1.5 on 2023-02-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameshop', '0009_alter_product_discout_id_alter_product_review_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='Product_images',
        ),
    ]
