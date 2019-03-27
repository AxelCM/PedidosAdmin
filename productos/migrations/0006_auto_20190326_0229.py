# Generated by Django 2.1.7 on 2019-03-26 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20190326_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id',
        ),
        migrations.AddField(
            model_name='categoria',
            name='id_categoria',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.Categoria'),
            preserve_default=False,
        ),
    ]