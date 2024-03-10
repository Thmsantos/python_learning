import imp
import mysql.connector
import os

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Thiago2004',
    database='produtos'
)

cursor = conexao.cursor()

print("O que deseja?")
print('-------------')  
print("Fazer comanda - (1)")
print('-------------')  
print("Gerenciar estoque - (2)")
print('-------------')  

decisao = int (input('1 ou 2: '))
os.system('cls') or None
total = 0

x = 0

z = 0

if decisao == 1 :
    total_teste = 0
    while (x == 0):

        print('-------------')  
        print("O que deseja?")
        print('-------------')  
        print("Café - (1)")
        print('-------------')  
        print("Chocolate quente - (2)")
        print('-------------') 
        print("Chá - (3)")
        print('-------------')  
        print("Cookie - (4)")
        print('-------------')
        valor = 0
        escolha = int (input('1, 2, 3 ou 4: '))
        os.system('cls') or None

        if escolha == 1 :

            comando = f'SELECT * FROM cafe'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print('-------------')
            print(resultado)
            print('-------------')
            id_del = (input('digite o id do cafe a ser adicionado na comanda: '))
            comando = f'DELETE FROM cafe WHERE id = {id_del}'
            cursor.execute(comando)
            conexao.commit()
            valor_local = float (input ('Valor: '))
            valor = valor + valor_local
            os.system('cls') or None
            """  print ('Deseja continuar? (0) sim, (1) não: ')
            y = float (input('0 ou 1: '))
            if y == 1:
                x = x + 1 """
            

        elif escolha == 2 :

            comando = f'SELECT * FROM chocolate'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print('-------------')
            print(resultado)
            print('-------------')
            id_del = (input('digite o id do chocolate a ser adicionado na comanda: '))
            comando = f'DELETE FROM chocolate WHERE id = {id_del}'
            cursor.execute(comando)
            conexao.commit()
            valor_local = float (input ('Valor: '))
            valor = valor + valor_local
            os.system('cls') or None
            """ print ('Deseja continuar? (0) sim, (1) não: ')
            y = float (input('0 ou 1: '))
            if y == 1:
                x = x + 1 """
            

        elif escolha == 3 :

            comando = f'SELECT * FROM cha'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print('-------------')
            print(resultado)
            print('-------------')
            id_del = (input('digite o id do cha a ser adicionado na comanda: '))
            comando = f'DELETE FROM cha WHERE id = {id_del}'
            cursor.execute(comando)
            conexao.commit()
            valor_local = float (input ('Valor: '))
            valor = valor + valor_local
            os.system('cls') or None
            """ print ('Deseja continuar? (0) sim, (1) não: ')
            y = float (input('0 ou 1: '))
            if y == 1:
                x = x + 1 """
            

        elif escolha == 4 :

            comando = f'SELECT * FROM cookie'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print('-------------')
            print(resultado)
            print('-------------')
            id_del = (input('digite o id do cookie a ser adicionado na comanda: '))
            comando = f'DELETE FROM cookie WHERE id = {id_del}'
            cursor.execute(comando)
            conexao.commit()
            valor_local = float (input ('Valor: '))
            valor = valor + valor_local
            os.system('cls') or None
            """  print ('Deseja continuar? (0) sim, (1) não: ')
            y = float (input('0 ou 1: '))
            if y == 1:
                x = x + 1 """            
        
        total_teste = total_teste + valor

        print('-------------')
        os.system('cls') or None
        print('Total: ',total_teste)
        print('-------------')
        print ('Deseja continuar? (0) sim, (1) não: ')
        y = float (input('0 ou 1: '))
        if y == 1:
            x = x + 1
    
elif decisao == 2 :
    
    while (z == 0):

        print('-------------')  
        print("Gerenciar cafés - (1)")
        print('-------------')  
        print("Gerenciar chocolates-quente - (2)")
        print('-------------')  
        print("Gerenciar chás - (3)")
        print('-------------')
        print("Gerenciar cookies - (4)")
        print('-------------')  

        opcao = int (input('1, 2, 3 ou 4: '))
        os.system('cls') or None

        if opcao == 1 :

            print('-------------')
            print("Inserir café - (1)")
            print('-------------')  
            print("Ver estoque de café - (2)")
            print('-------------')  
            print("Atualizar nome do café - (3)")
            print('-------------')
            print("Atualizar valor do café - (4)")
            print('-------------')
            print("excluir café - (5)")
            print('-------------')
            print("Ver quantidade de cafés - (6)")
            print('-------------')

            decisao_cafe = int (input('1, 2, 3, 4, 5 ou 6: '))
            os.system('cls') or None

            if decisao_cafe == 1 :
                nome = str (input('Nome do café a ser inserido: '))
                valor = float (input('Valor do café a ser inserido: '))
                comando = f'INSERT INTO CAFE (nome_cafe, valor) VALUES ("{nome}", {valor})'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Inserido com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cafe == 2 :
                comando = f'SELECT * FROM cafe'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

            elif decisao_cafe == 3 :
                comando_id = f'SELECT id, nome_cafe FROM cafe'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_cafe = int (input('digite o id do cafe a ser modificado: '))
                nome_mod = str (input('Novo nome do cafe: '))
                comando = f'UPDATE cafe SET nome_cafe = "{nome_mod}" WHERE id = "{id_cafe}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cafe == 4 :
                comando_id = f'SELECT id, nome_cafe FROM cafe'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_cafe = int (input('digite o id do cafe a ser modificado: '))
                valor_mod = float (input('Novo valor: '))
                comando = f'UPDATE cafe SET valor = {valor_mod} WHERE id = "{id_cafe}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cafe == 5 :
                comando_id = f'SELECT id, nome_cafe FROM cafe'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print(resultado)
                print('-------------')
                id_del = (input('digite o id do cafe a ser excluído: '))
                comando = f'DELETE FROM cafe WHERE id = {id_del}'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Excluído com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cafe == 6 :
                comando = f'select count(nome_cafe) from cafe'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print('quantidade: ',resultado)
                print('-------------')  
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

        elif opcao == 2 :

            print('-------------')
            print("Inserir chocolate - (1)")
            print('-------------')  
            print("Ver estoque de chocolate - (2)")
            print('-------------')  
            print("Atualizar nome do chocolate - (3)")
            print('-------------')
            print("Atualizar valor do chocolate - (4)")
            print('-------------')
            print("excluir chocolate - (5)")
            print('-------------')
            print("Quantidades de chocolate - (6)")
            print('-------------')
            
            decisao_chocolate = int (input('1, 2, 3, 4, 5 ou 6: '))
            os.system('cls') or None

            if decisao_chocolate == 1 :
                nome = str (input('Nome do chocolate a ser inserido: '))
                valor = float (input('Valor do chocolate a ser inserido: '))
                comando = f'INSERT INTO CHOCOLATE (nome_chocolate, valor) VALUES ("{nome}", {valor})'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Inserido com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_chocolate == 2 :
                comando = f'SELECT * FROM chocolate'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

            elif decisao_chocolate == 3 :
                comando_id = f'SELECT id, nome_chocolate FROM chocolate'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_chocolate = int (input('digite o id do chocolate a ser modificado: '))
                nome_mod = str (input('Novo nome do chocolate: '))
                comando = f'UPDATE chocolate SET nome_chocolate = "{nome_mod}" WHERE id = "{id_chocolate}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_chocolate == 4 :
                comando_id = f'SELECT id, nome_chocolate, valor FROM chocolate'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_chocolate = int (input('digite o id do chocolate a ser modificado: '))
                valor_mod = float (input('Novo valor: '))
                comando = f'UPDATE chocolate SET valor = {valor_mod} WHERE id = "{id_chocolate}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_chocolate == 5 :
                comando_id = f'SELECT id, nome_chocolate FROM chocolate'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print(resultado)
                print('-------------')
                id_del = (input('digite o id do chocolate a ser excluído: '))
                comando = f'DELETE FROM chocolate WHERE id = {id_del}'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Excluído com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_chocolate == 6 :
                comando = f'select count(nome_chocolate) from chocolate'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print('quantidade: ',resultado)
                print('-------------')  
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

        
        elif opcao == 3 :

            print("Inserir chá - (1)")
            print('-------------')  
            print("Ver estoque de chá - (2)")
            print('-------------')  
            print("Atualizar nome do chá - (3)")
            print('-------------')
            print("Atualizar valor do chá - (4)")
            print('-------------')
            print("excluir chá - (5)")
            print('-------------')
            print("Ver quantidade de chás - (6)")
            print('-------------')

            decisao_cha = int (input('1, 2, 3, 4, 5 ou 6: '))
            os.system('cls') or None

            if decisao_cha == 1 :
                nome = str (input('Nome do chá a ser inserido: '))
                valor = float (input('Valor do chá a ser inserido: '))
                comando = f'INSERT INTO CHA (nome_cha, valor) VALUES ("{nome}", {valor})'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Inserido com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cha == 2 :
                comando = f'SELECT * FROM cha'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

            elif decisao_cha == 3 :
                comando_id = f'SELECT id, nome_cha FROM cha'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_cha = int (input('digite o id do chá a ser modificado: '))
                nome_mod = str (input('Novo nome do chá: '))
                comando = f'UPDATE cha SET nome_cha = "{nome_mod}" WHERE id = "{id_cha}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cha == 4 :
                comando_id = f'SELECT id, nome_cha, valor FROM cha'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_cha = int (input('digite o id do cha a ser modificado: '))
                valor_mod = float (input('Novo valor: '))
                comando = f'UPDATE cha SET valor = {valor_mod} WHERE id = "{id_cha}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cha == 5 :
                comando_id = f'SELECT id, nome_cha FROM cha'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print(resultado)
                print('-------------')
                id_del = (input('digite o id do chá a ser excluído: '))
                comando = f'DELETE FROM cha WHERE id = {id_del}'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Excluído com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cha == 6 :
                comando = f'select count(nome_cha) from cha'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print('quantidade: ',resultado)
                print('-------------')  
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
        

        elif opcao == 4 :

            print("Inserir cookie - (1)")
            print('-------------')  
            print("Ver estoque de cookie - (2)")
            print('-------------')  
            print("Atualizar nome do cookie - (3)")
            print('-------------')
            print("Atualizar valor do cookie - (4)")
            print('-------------')
            print("excluir cookie - (5)")
            print('-------------')
            print("Verficar quantidade de cookies - (6)")
            print('-------------')

            decisao_cookie = int (input('1, 2, 3, 4, 5 ou 6: '))
            os.system('cls') or None
 
            if decisao_cookie == 1 :
                nome = str (input('Nome do cookie a ser inserido: '))
                valor = float (input('Valor do cookie a ser inserido: '))
                comando = f'INSERT INTO cookie (nome_cookie, valor) VALUES ("{nome}", {valor})'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Inserido com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cookie == 2 :
                comando = f'SELECT * FROM cookie'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

            elif decisao_cookie == 3 :
                comando_id = f'SELECT id, nome_cookie FROM cookie'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_cookie = int (input('digite o id do cookie a ser modificado: '))
                nome_mod = str (input('Novo nome do cookie: '))
                comando = f'UPDATE cookie SET nome_cookie = "{nome_mod}" WHERE id = "{id_cookie}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cookie == 4 :
                comando_id = f'SELECT id, nome_cookie, valor FROM cookie'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print('-------------')
                print(resultado)
                print('-------------')
                id_cookie = int (input('digite o id do cookie a ser modificado: '))
                valor_mod = float (input('Novo valor: '))
                comando = f'UPDATE cookie SET valor = {valor_mod} WHERE id = "{id_cookie}"'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Atualizado com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None
            
            elif decisao_cookie == 5 :
                comando_id = f'SELECT id, nome_cookie FROM cookie'
                cursor.execute(comando_id)
                resultado = cursor.fetchall()
                print(resultado)
                print('-------------')
                id_del = (input('digite o id do cookie a ser excluído: '))
                comando = f'DELETE FROM cookie WHERE id = {id_del}'
                cursor.execute(comando)
                conexao.commit()
                print('-------------')  
                print('Excluído com sucesso!')
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

            elif decisao_cookie == 6 :
                comando = f'select count(nome_cookie) from cookie'
                cursor.execute(comando)
                resultado = cursor.fetchall()
                print('-------------')
                print('quantidade: ',resultado)
                print('-------------')  
                print ('Deseja continuar? (0) sim, (1) não: ')
                y = float (input('0 ou 1: '))
                if y == 1:
                    z = z + 1
                os.system('cls') or None

cursor.close()
conexao.close()