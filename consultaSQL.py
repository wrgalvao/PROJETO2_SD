import mysql.connector

con = mysql.connector.connect(host='localhost', database='hotel', user = 'wrgalvao', password = '81623140')
consultaSQL = "select * from quarto"
cursor = con.cursor()
cursor.execute(consultaSQL)
linhas = cursor.fetchall()
print("Numero total de registros retornados: ", cursor.rowcount)
for linha in linhas:
    print("Quantidade de quartos Disponiveis ", linha[0])
if(con.is_connected()):
    con.close()
    cursor.close()
    print("Conexao ao mysql encerrada")