# Importando o driver de Banco de Dados
import mysql.connector

def DBconfig():
    conexao = mysql.connector.connect(
        host="localhost",
        user="admin",
        database="mybusinessdb",
        password="123456"
    )

    return conexao
