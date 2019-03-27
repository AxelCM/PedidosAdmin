# Generated by Django 2.1.7 on 2019-03-27 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20190327_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='id_pedido',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='id_pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedidos.PedidoVentas'),
            preserve_default=False,
        ),
    ]