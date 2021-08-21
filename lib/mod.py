from datetime import date
import pandas as pd
import datetime

 #   A) Criação da classe 'MinhaData'
class MinhaData(object):
    def __init__(self, dia, mes=0, ano=0):                   #   B) Criação do construtor recebendo 3 valores
        self.dia = dia
        if type(self.dia)==int:                 
            self.dia = dia
            self.mes = mes
            self.ano = ano
        else:                                                #   C) Em python não existe forma de criar um segundo construtor igual em Java,
            dias = self.dia.split('/')                       #   Porém a solução abordada foi o controle maior dos argumentos
            self.dia = int(dias[0])
            self.mes = int(dias[1])
            self.ano = int(dias[2])

#   D) Criação do método toString() para representação do objeto data
    def __repr__(self):                                       
        return str(f'{self.dia}/{self.mes}/{self.ano}')

#   E) Criação do método Adicionar ou Diminuir, para modificar o objeto data

    def ADDSUB(self, parametro, opcao, valor):
        data_str = str(f'{self.dia}/{self.mes}/{self.ano}')
        data_mod = datetime.datetime.strptime(data_str,'%d/%m/%Y')
        if opcao == 'somar':
            if parametro == 'dia':
                data_nova = data_mod + datetime.timedelta(days=valor)
            elif parametro == 'mes':
                data_nova = data_mod + pd.DateOffset(months=valor)
            elif parametro == 'ano':
                data_nova = data_mod + pd.DateOffset(years=valor)
        elif opcao == 'diminuir':
            if parametro == 'dia':
                data_nova = data_mod - datetime.timedelta(days=valor)
            elif parametro == 'mes':
                data_nova = data_mod - pd.DateOffset(months=valor)
            elif parametro == 'ano':
                data_nova = data_mod - pd.DateOffset(years=valor)
                
        return data_nova.strftime('%d/%m/%Y')
        
                



#  F) Criação do metodo 'Compara' 
    def Compara(self, data_compara):                        
        n1 = self.dia+(self.mes*30)+(self.ano*365)
        n2 = data_compara.dia+(data_compara.mes*30)+(data_compara.ano*365)

        if n1 == n2:
            return 0        #   Retornado 0, caso a data comparada seja igual
        elif n1 > n2:
            return 1        #   Retornado 1, caso a data comparada seja antecedente
        else:
            return -1       #   Retornando -1, caso a data comparada seja posterior


#   G) Criação da classe 'DataComemorativa', recebendo 'Nome', 'dia', 'mes', 'ano' e o valor 'True' ou 'False' para caso seja feriado e/ou mundial 
class DataComemorativa(object):
    def __init__(self, nome_data, dia, mes, ano, feriado=False, mundial=False):
        self.nome_data = nome_data
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.feriado = feriado
        self.mundial = mundial

class DataspraLista():
    def __init__(self, data):
        self.lst = []
        self.lst.append(data.nome_data)
        self.lst.append(data.dia)
        self.lst.append(data.mes)        ##faz herança nessa porra
        self.lst.append(data.feriado)
        self.lst.append(data.mundial)

#   H)  Criação da classe 'DatasComemorativas', armazenando em lista as datas criadas
class DatasComemorativas(DataspraLista):
    def __init__(self, data):
        DataspraLista.__init__(self, data)
        self.lista = []

    def __repr__(self):                                       
        return f'{self.lista[0]}'

#   I)  Método que adiciona o objeto do tipo 'DataComemorativa' à lista
    def Adiciona(self, data):
        for z in self.lista:                #   Teste para caso ocorra uma inserção duplicada
            if z[0] == data.nome_data:
                print(f'ERRO: O dia {data.nome_data} já foi adicionado a coleção!')
                return
    
        self.lista.append(DataspraLista(data).lst)
        return

#   J)  Método que remove um objeto do tipo 'DataComemorativa' da lista recebendo como parâmetro o nome da data
    def Remover(self, nomedata):
        for k,z in enumerate(self.lista):
            if z[0] == nomedata:
                del self.lista[k]
                return True
        return False

#   K)  Método que retorna as horas não trabalhadas com base no valor da variável 'Feriado'
    def HorasNaoTrabalhadas(self):
        horas = 0
        for y in self.lista:
            if y[3]==True:
                horas += 8
        return horas
        