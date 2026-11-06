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

def resumo_tratamento():
    resultado = []
    for linha in listar_medicamentos():
        nome = linha[1]
        posologia = linha[2]
        proxima_data = proxima_dose(nome)
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
        resultado.append({'medicamento': nome, 'posologia': posologia, 'proxima_dose': proxima, 'final_do_tratamento': final})
    return resultado

            
    



def alarme_medicamento(medicamento):
    proxima_dose = intervalo_medicamento(medicamento)
    if not proxima_dose:
        yield f"Não foi possível determinar o horário da próxima dose do medicamento {medicamento}."
        return
    
    limite = proxima_dose + datetime.timedelta(minutes=10)
    
    while True:
        if tomou.is_set():
            yield f"Dose do medicamento {medicamento} confirmada."
            break
        horario_atual = datetime.datetime.now()
        if horario_atual >= limite:
            yield f"Hora de tomar o medicamento {medicamento}!"
                
        elif horario_atual < proxima_dose: 
            yield f"Faltam {proxima_dose - horario_atual} para a próxima dose do medicamento {medicamento}."
        else:
            atraso = horario_atual - proxima_dose
            yield f'voce perdeu a hora de tomar o medicamento {medicamento}! Atraso de {atraso}.'
        tomou.wait(60)       

def tempo_restante(inicio, tempo):
    inicio = datetime.datetime.fromisoformat(inicio)
    fim = inicio + datetime.timedelta(days=tempo)
    tempo_restante = fim - datetime.datetime.now()
    if tempo_restante <= datetime.timedelta(days=0):
        return None
    else:
        return tempo_restante
 