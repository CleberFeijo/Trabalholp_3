from datetime import date 
import datetime                  # Modulo referente à acquisição do dia atual
from lib.mod import MinhaData               # Modulos referente às classes criadas
from lib.mod import DataComemorativa
from lib.mod import DatasComemorativas

data_hoje = date.today()
data = data_hoje.strftime('%d/%m/%Y')

#   L)I) Data atual:
#        Padrão:'%d/%m/%Y' 

hoje = MinhaData(data)
# print(hoje)

#   L)I) Criação da data comemorativa 'Natal'
natal = DataComemorativa('Natal',25,12,int(data_hoje.strftime('%Y')),True,True)

# pascoa = DataComemorativa('Pascoa',30,4,int(data_hoje.strftime('%Y')),True,True)

# data_nova = MinhaData(hoje.ADDSUB('dia', 'somar', 43))
# print(data_nova)
# data_nova = MinhaData(data_nova.ADDSUB('mes', 'diminuir', 11))
# print(data_nova)
# data_nova = MinhaData(data_nova.ADDSUB('ano', 'somar', 21))
# print(data_nova)


#   Ex.: Data genérica:
#        Padrão: dia, mês, ano
# dia_30_5_1999 = MinhaData(30,5,1999)
# print(hoje)
# print(dia_30_5_1999)

#   L)II) Comparação do dia atual com o natal e 'print' do valor
print(hoje.Compara(natal))

#   L)III) Criação da coleção de datas comemorativas
colecao_datas_comemorativas = DatasComemorativas(natal)

#   L)III) Adicionando natal à coleção
colecao_datas_comemorativas.Adiciona(natal)
# colecao_datas_comemorativas.Adiciona(pascoa)

#   L)III) 'print' das horas não trabalhadas
print(colecao_datas_comemorativas.HorasNaoTrabalhadas())

