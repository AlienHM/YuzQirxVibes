# Generated by Django 4.0.6 on 2022-08-10 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YuzQirxApp', '0012_remove_product_image_productimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
    ]
