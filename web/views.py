from django.shortcuts import render
from .models import Aluno
from .models import Professor
from .models import Telefone
from django.http import HttpResponse

def alunos(request):
    lista_alunos = Aluno.objects.all()
    retorno = ''
    for aluno in lista_alunos:
        tel = Telefone.objects.get(pk = aluno.id_telefone)
        #.x =
        retorno += "Nome = " , aluno.nome , " -- Numero = " , str(
            tel.privado()) , " -- Curso = " , aluno.curso," -- hras no curso = " , \
                   str(aluno.horasTotais(aluno.nPeriodos, aluno.nHraPeriodo)),"<br/>"
    return HttpResponse(retorno)

def alunox(request, id):
    aluno = Aluno.objects.get(pk = id)
    tel = Telefone.objects.get(pk = aluno.id_telefone)
    return HttpResponse("Nome = " + str(aluno.nome) + " -- Numero = " + str(
            tel.privado()) + " -- Curso = " + str(aluno.curso) + " -- hras no curso = " + \
                   str(aluno.horasTotais(aluno.nPeriodos, aluno.nHraPeriodo)))

def professores(request):
    lista_prof = Professor.objects.all()
    retorno = ''
    for prof in lista_prof:
        tel = Telefone.objects.get(pk = prof.id_telefone)
        retorno += "Nome = " + str(prof.nome) + " -- Numero = " + str(
            tel.privado()) + " -- Curso = " + str(prof.curso) + " -- hras aulas = " + \
                   str(prof.horasTotais(prof.nAula, prof.nHraAula)) + "<br/>"
    return HttpResponse(retorno)

def professorx(request, id):
    prof = Professor.objects.get(pk=id)
    tel = Telefone.objects.get(pk=prof.id_telefone)
    return HttpResponse("Nome = " + str(prof.nome) + " -- Numero = " + str(
            tel.privado()) + " -- Curso = " + str(prof.curso) + " -- hras aulas = " + \
                   str(prof.horasTotais(prof.nAula, prof.nHraAula)))