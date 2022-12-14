# Generated by Django 4.1.2 on 2022-10-17 16:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField(default=django.utils.timezone.now)),
                ('data_entrega', models.DateField(null=True)),
                ('data_devolução', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StatusPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PedidoCloncluido',
            fields=[
                ('pedido_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pedidos.pedido')),
                ('preco_final', models.FloatField()),
                ('data_conclusão', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
            bases=('pedidos.pedido',),
        ),
    ]
