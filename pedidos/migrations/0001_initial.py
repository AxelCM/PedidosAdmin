# Generated by Django 2.1.7 on 2019-03-27 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0007_movimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoVentas',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Fecha de Pedido')),
                ('date_des', models.DateField(auto_now_add=True, verbose_name='Fecha de Despacho')),
                ('cantidad_pedida', models.IntegerField(default=0, verbose_name='Cantidad Pedida')),
                ('cantidad_entregada', models.IntegerField(default=0, verbose_name='Cantidad Entregada')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
    ]
