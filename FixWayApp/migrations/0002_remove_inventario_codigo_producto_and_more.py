# Generated by Django 5.0.6 on 2024-09-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FixWayApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='codigo_producto',
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ano_producto_uso_fin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ano_producto_uso_inicio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='costo',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='marca_automovil',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='marca_producto',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='origen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='precio_detalle',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
