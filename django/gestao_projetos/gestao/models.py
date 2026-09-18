from django.db import models
from datetime import datetime

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    # descricao = models.TextField(blank=True, null = True) Não obrigatório
    data_inicio = models.DateField(default=datetime.now)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    prazo_conclusao = models.DateField()
    projeto_vinculado = models.ForeignKey(Projeto, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo