from conexao import connect

def insert(mydb, titulo, autor):
    mycursor = mydb.cursor()

    sql = "INSERT INTO livros (titulo, autor) VALUES (%s, %s)"
    val = (titulo, autor)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()