from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name="Data do Evento")
    local = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True, verbose_name="Data de Criação")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Evento"
        managed = True
        verbose_name = "evento"
        verbose_name_plural = "eventos"

        def __str__(self):
            return self.titulo


def get_data_evento(self):
    return self.data_evento.strftime("%d/%m/%Y %H:%M")


def get_evento_atrasado(self):
    return self.data_evento < datetime.now()


def get_evento_que_falta_menos_de_1h(self):
    return (
        datetime.now() > self.data_evento - timedelta(hours=1)
        and datetime.now() < self.data_evento
    )
