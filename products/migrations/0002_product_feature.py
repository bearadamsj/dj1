# Generated by Django 3.1.7 on 2021-03-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
