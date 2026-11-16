from database import *
import datetime


def inicio_tratamento(medicamento):
    inicio = datetime.datetime.fromisoformat(listar_inicio_medicamento(medicamento)[0])
    return inicio

def intervalo_medicamento(medicamento):
    posologia = listar_posologia_medicamento(medicamento)[0]
    intervalo = 24/posologia
    return intervalo

def fim_tratamento_medicamento(medicamento):
    inicio = inicio_tratamento(medicamento)
    tempo = listar_tempo_medicamento(medicamento)[0]
    fim = inicio + datetime.timedelta(days=tempo)
    return fim

def proxima_dose(medicamento):
    inicio = inicio_tratamento(medicamento)
    fim = fim_tratamento_medicamento(medicamento)
    intervalo = intervalo_medicamento(medicamento)  
    tratamento = inicio + datetime.timedelta(hours=intervalo)
    while tratamento <= fim:
        if tratamento >= datetime.datetime.now():
            return tratamento
        else:
            tratamento += datetime.timedelta(hours=intervalo)
    return None

def formatar_duracao(duracao):
    final = duracao.replace('day', 'dia')
    return final



            
def ultima_dose_passada(medicamento):
    inicio = inicio_tratamento(medicamento)
    fim = fim_tratamento_medicamento(medicamento)
    intervalo = intervalo_medicamento(medicamento)  
    tratamento = inicio + datetime.timedelta(hours=intervalo)
    ultima_dose = None
    while tratamento <= fim:
        if tratamento <= datetime.datetime.now():
            ultima_dose = tratamento
        else:
            break
        tratamento += datetime.timedelta(hours=intervalo)
    return ultima_dose

def formatar_horario_dose(horario):
    if horario is None:
        return None
    else:
        return horario.strftime("%Y-%m-%d %H:%M")

    
def estado_dose(medicamento_id, nome):
    agora = datetime.datetime.now()
    ultima= ultima_dose_passada(nome)
    if fim_tratamento_medicamento(nome) < agora:
        return "Finalizado"
    elif ultima is None:
        return "Aguardando"
    elif dose_confirmada(medicamento_id, formatar_horario_dose(ultima)):
        return "Confirmado"
    else:
        if agora - ultima > datetime.timedelta(minutes=10):
            return "Atrasado"
        else: 
            return "Hora_de_tomar"


def resumo_tratamento():
    resultado = []
    for linha in listar_medicamentos():
        id = linha[0]
        nome = linha[1]
        posologia = linha[2]
        proxima_data = proxima_dose(nome)
        estado = estado_dose(id, nome)
        if proxima_data:
            proxima = proxima_data - datetime.datetime.now()
            proxima = str(proxima).split('.')[0]
        else:
            proxima = None
        final = fim_tratamento_medicamento(nome) - datetime.datetime.now()
        if final <= datetime.timedelta(days=0):
            final = None
        else: 
            final = str(final).split('.')[0]
            final = formatar_duracao(final)
        resultado.append({'medicamento': nome, 'posologia': posologia, 'proxima_dose': proxima, 'final_do_tratamento': final, 'id': id, 'estado': estado})
    return resultado