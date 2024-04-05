from conexao_amelyne import connect
from funcao_amelyne import insert

mydb = connect()

t = 'Game of Devops 3'
a = 'Jhonathan Rennan'
insert(mydb, t, a)

mydb.close()