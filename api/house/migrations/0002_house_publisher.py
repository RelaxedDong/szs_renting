# Generated by Django 2.0 on 2019-06-11 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
    ]
