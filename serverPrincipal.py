from msilib.schema import Error
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import mysql.connector
from mysql.connector import Error
print('cliente')
ip = input('Digite o ip do servidor: ')
porta = int(input('Digite a porta do servidor: '))
servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(ip, porta))
while(True):
    resposta = input('Deseja realizar uma consulta de quarto s/n ?')
    resposta.lower()
    if(resposta == 's'):
        quantidadeDisponivel = servidor.buscarQuartoDisponivel()
        print("Quartos Disponiveis: ",quantidadeDisponivel)
        #consultaQuartos = servidor.buscarQuartoDisponivel()
        #print("Quantidade de quartos disponiveis e: ", consultaQuartos)
    elif(resposta == 'n'):
        break
