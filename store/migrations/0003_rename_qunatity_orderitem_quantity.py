# Generated by Django 3.2.3 on 2021-05-13 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_porduct_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
