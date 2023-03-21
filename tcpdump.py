#Aluna: Laura Thaís Gomes da Silva Batista - 20192014050017
import struct
import datetime
#Aqui eu li o arquivo, me posicionei onde precisava começar a ler e de fato iniciei a leitura
fd = open("cap2.dump", "rb")
cabArq = fd.seek(24)
cabPak = fd.read(16)

#abaixo estão as variáveis e listas que usei no código
timestamp = []
tamanho = []
tamanhoT = []
qtd = 0

#começando o tratamento dos dados dos cabeçalhos dos pacotes
while cabPak != b'':
    cabecalho = struct.unpack("<iiii", cabPak)#desempacotei as informações do cabeçalho para inteiro
    #print(cabecalho)
    #Criei as listas com as informações que iria usar depois
    timestamp.append(cabecalho[0])
    tamanho.append(cabecalho[2])
    tamanhoT.append(cabecalho[3])
    #esse if foi feito aqui para responder a questão 3.
    if cabecalho[2] != cabecalho[3]:
        qtd += 1
    novaposicao = fd.read(cabecalho[2])#encontrei a nova posição para ler o próximo cabeçalho
    cabPak = fd.read(16)
fd.close()
#Resposta da Questão 1
print("A captura começa em: ", datetime.datetime.fromtimestamp(timestamp[0]),
      "e termina em: ", datetime.datetime.fromtimestamp(sorted(timestamp, reverse=True)[0]))
#Resposta da Questão 2
print("O tamanho do maior pacote capturado foi de: ", max(tamanho))

#Resposta da Questão 3
print(qtd, " pacotes não foram salvos totalmente")

#Resposta da Questão 4
print("O tamanho médio dos pacotes capturados foi de: ", sum(tamanhoT)/ len(tamanhoT))