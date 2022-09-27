from msilib.schema import Error
from xmlrpc.server import SimpleXMLRPCServer
import mysql.connector
from mysql.connector import Error
print('SERVIDOR')
ip = '127.0.0.1'
porta = 8080
def buscarQuartoDisponivel():
    con = mysql.connector.connect(host = 'localhost', database='hotel', user = 'wrgalvao', password = '81623140')
    consultaSQL = "select * from quarto"
    cursor = con.cursor()
    cursor.execute(consultaSQL)
    linhas = cursor.fetchall()
#    print("Numero total de registros retornados: ", cursor.rowcount)
    for linha in linhas:
        quantidadeDisponivel = linha[0]
    if(con.is_connected()):
        con.close()
        cursor.close()
#        print("Conexao ao mysql encerrada")
    return quantidadeDisponivel
def iniciarRPC():
    print('Servidor iniciado, esperando por clientes em:\nip: 127.0.0.1\nporta: 8080')
    servidor = SimpleXMLRPCServer((ip, porta))
    servidor.register_function(buscarQuartoDisponivel, "buscarQuartoDisponivel")
    servidor.serve_forever()