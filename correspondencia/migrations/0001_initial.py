# Generated by Django 3.2.16 on 2022-10-07 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('sigla', models.CharField(max_length=50, unique=True)),
                ('estado', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('abreviatura', models.CharField(max_length=50, unique=True)),
                ('cite', models.CharField(max_length=100, unique=True)),
                ('estado', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cite', models.CharField(max_length=100, unique=True)),
                ('referencia', models.TextField()),
                ('estado', models.CharField(choices=[('habilitado', 'Habilitado'), ('anulado', 'Anulado')], default='habilitado', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='correspondencia.oficina')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='correspondencia.tipo')),
                ('usaurio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documento_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Correlativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlativo', models.IntegerField(default=0)),
                ('gestion', models.IntegerField(default=0)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='correspondencia.oficina')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='correspondencia.tipo')),
            ],
        ),
    ]