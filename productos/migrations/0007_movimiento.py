# Generated by Django 2.1.7 on 2019-03-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_auto_20190326_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id_movimiento', models.AutoField(primary_key=True, serialize=False)),
                ('c_entrada', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('c_salida', models.IntegerField(default=0, verbose_name='Cantidad')),
            ],
        ),
    ]
