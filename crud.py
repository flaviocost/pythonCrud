import mysql.connector

def menu():
    print("MENU")
    print("=" * 35)
    print("[1] Inserir")
    print("[2] Remover")
    print("[3] Procurar")
    print("[0] Sair")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="desafioacademia"
)
mycursor = mydb.cursor()
loop = True
while loop:
    menu()
    choice = input("Digite o dígito da operação que deseja efetuar: ")
    while True:
        print("Escolha uma das opções abaixo!")
        print("[1] Aluno")
        print("[2] Funcionário")
        print("[3] Modalidade")
        print("[4] Personal")
        type = int(input("Digite aqui: "))
        if type == 1:
            table = "alunos"
            break
        if type == 2:
            table = "funcionarios"
            break
        if type == 3:
            table = "modalidades"
            break
        if type == 4:
            table = "personal"
            break
        else:
            print("Digite um dígito válido.")
    #Inserir
    if choice == "1":
        if table == "alunos":
            nome_alunos = input("NOME: ")
            cpf = input("CPF: ")
            telefone = input("TELEFONE: ")
            endereco = input("ENDEREÇO: ")
            email = input('E-MAIL: ')
            val = (nome_alunos, cpf, telefone, endereco, email)
            sql = "INSERT INTO alunos (nome_alunos, cpf, telefone, endereco, email) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()
            print(" Aluno adicionado!")

        if table == "personal":
            cpf = input("CPF: ")
            nome = input("NOME: ")
            cref = input("CREF: ")
            endereco = input("ENDEREÇO: ")
            telefone = input("TELEFONE: ")
            email = input('E-MAIL:')

            val = (cpf, nome, cref, endereco, telefone, email)
            sql = "INSERT INTO personal (cpf, nome, cref, endereco, telefone, email) VALUES (%s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()
            print("Personal adicionado!")

        if table == "funcionarios":
            nome = input("NOME:: ")
            cpf = input("CPF: ")
            salario = input("SALARIO: ")
            val = (nome, cpf, salario)
            sql = "INSERT INTO funcionarios (nome, cpf, salario) VALUES (%s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()
            print("Funcionario adicionado!")

        if table == "modalidades":
            id_matricula = input("Digite o nome da modalidade: ")
            nome = input("NOME: ")
            duracao = input("DURAÇÃO: ")
            val = (id_matricula, nome, duracao)
            sql = "INSERT INTO modalidades (id_matricula, nome, duracao) VALUES (%s, %s, %s)"
            mycursor.execute(sql, val)
            mydb.commit()

            print("Modalidades adicionado!")
    #Remover
    elif choice == "2":
        if table == "alunos":
            valor = input("Digite a matrícula do aluno que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("Aluno removido!")
        if table == "personal":
            valor = input("Digite o CREF do personal que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("=" * 35)
            print("Personal removido!")
        if table == "funcionarios":
            valor = input("Digite o ID do funcionário que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("Funcionario removido!")
        if table == "modalidades":
            valor = input("Digite o ID da modalidade que deseja remover: ")
            val = (valor, )
            sql = f"DELETE FROM {table} WHERE id = %s"
            mycursor.execute(sql, val)
            mydb.commit()
            print("Modalidade removido!")
    #Procurar
    elif choice == "3":
        if table == "alunos":
            mycursor.execute(f"SELECT * FROM {table}")
            resultado = mycursor.fetchall()

            for aluno in resultado:
                print(f"MATRÍCULA: {aluno[0]}")
                print(f"NOME: {aluno[1]}")
                print(f"TELEFONE: {aluno[2]}")
                print(f"ENDEREÇO: {aluno[3]}")
                print(f"CPF: {aluno[4]}")
                print(f"EMAIL: {aluno[5]}")
        if table == "personal":
            mycursor.execute(f"SELECT * FROM {table}")
            resultado = mycursor.fetchall()

            for personal in resultado:
                print(f"NOME: {personal[0]}")
                print(f"CPF: {personal[1]}")
                print(f"CREF: {personal[2]}")
                print(f"TELEFONE: {personal[3]}")
                print(f"ENDEREÇO: {personal[4]}")
        if table == "modalidades":
            mycursor.execute(f"SELECT id, nome, descricao, duracao FROM {table}")
            resultado = mycursor.fetchall()

            for modalidade in resultado:
                print(f"ID: {modalidade[0]}")
                print(f"NOME: {modalidade[1]}")
                print(f"DESCRIÇÃO: {modalidade[2]}")
                print(f"DURAÇÃO: {modalidade[3]}")
        if table == "funcionarios":
            mycursor.execute(f"SELECT id, nome, cpf, salario FROM {table}")
            resultado = mycursor.fetchall()

            for funcionario in resultado:
                print(f"ID: {funcionario[0]}")
                print(f"NOME: {funcionario[1]}")
                print(f"CPF: {funcionario[2]}")
                print(f"SALÁRIO: {funcionario[3]}")
    elif choice == "4":
        while True:
            doubt = input("Desje sair? \n"
                          "[1] - Para sair"
                          "[2] - Para voltar ao menu \n"
                          "Opção de escolha: ")
            if doubt != "1" and doubt != "2":
                ...
            else:
                break
        if doubt == "1":
            break
        if doubt == "2":
            ...
print("Programa finalizado!")