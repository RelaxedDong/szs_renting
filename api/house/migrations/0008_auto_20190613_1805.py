# Generated by Django 2.0 on 2019-06-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_auto_20190613_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='facilities',
            field=models.TextField(default={}, verbose_name='设施'),
        ),
    ]
