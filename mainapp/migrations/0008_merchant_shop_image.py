# Generated by Django 3.1.2 on 2020-10-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_merchant'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='shop_image',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
