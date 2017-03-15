from django.db import models

# Create your models here.

class Endereco(models.Model):
    cidade = models.CharField('cidade', max_length=200)
    quadra = models.CharField('quadra', max_length=200)
    endereco = models.CharField('endereco', max_length=200)
    lote = models.CharField('lote', max_length=200)

class Telefone(models.Model):
    numero = models.CharField('numero', max_length=11, null = True)

    @property
    def privado(self):
        return self.numero

    @privado.setter
    def privado(self, value):
        self.numero = value


class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=200)
    id_telefone = models.IntegerField('telefone')
    id_endereco = models.IntegerField('id_endereco')

    def horasTotais(self):
        raise NotImplementedError(
            "Subclasses precisam implementar o metodo abstrato"
        )

class Aluno(Pessoa):
    curso = models.CharField('curso', max_length=200)
    nPeriodos = models.IntegerField('nPeriodos')
    nHraPeriodo = models.IntegerField('nHraPeriodo')

    def horasTotais(self, nP, nH):
        return nP*nH

class Professor(Pessoa):
    curso = models.CharField('curso', max_length=200)
    nAula = models.IntegerField('nPeriodos')
    nHraAula = models.IntegerField('nHraPeriodo')

    def horasTotais(self, nP, nH):
        return nP*nH

