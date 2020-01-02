# Generated by Django 2.2.7 on 2020-01-02 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pixel', '0002_pagevisit_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagevisit',
            name='referer',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='pagevisit',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pixel.Domain'),
        ),
    ]
