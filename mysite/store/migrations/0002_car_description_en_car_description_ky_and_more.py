# Generated by Django 5.1 on 2024-08-25 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='product_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='product_name_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='product_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
