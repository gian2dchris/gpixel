# Generated by Django 2.2.7 on 2020-01-05 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0007_auto_20200105_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='maintainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to=settings.AUTH_USER_MODEL),
        ),
    ]