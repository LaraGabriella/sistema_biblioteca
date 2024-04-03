from conexao import connect
from funcao import insert

# Conectar ao banco de dados
mydb = connect()

# Chamar a função insert_customer com os valores desejados
t = 'Game of Devops 3'
a = 'Jhonathan Rennan'
insert(mydb, t, a)

# Fechar a conexão com o banco de dados
mydb.close()