# Generated by Django 4.0.4 on 2022-05-18 20:43

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
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField(verbose_name='Data do Evento')),
                ('local', models.TextField(blank=True, null=True)),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data de Criação')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'evento',
                'verbose_name_plural': 'eventos',
                'db_table': 'Evento',
                'managed': True,
            },
        ),
    ]
