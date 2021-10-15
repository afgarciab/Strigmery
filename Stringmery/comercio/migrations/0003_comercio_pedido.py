# Generated by Django 3.2.6 on 2021-10-15 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
        ('comercio', '0002_comercio_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='pedido',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido'),
        ),
    ]
