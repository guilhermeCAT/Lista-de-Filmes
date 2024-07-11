import os 

nome = input("Qual seu nome? ")
os.system('cls')
print(f'bem vindo {nome}')

filmes = [[],[],[],[],[]]

while True:
    try:
        print(f'deseja ver a lista de filmes ?')
        menu = input('qual sua escolha: [1]sim [2]não: ') 
        menu_int = int(menu)
        os.system('cls')

        if menu_int == 0:
            print("somente 1 ou 2")
            continue
        elif menu_int == 2:
             print("voce saiu.")
             break        
        elif menu_int > 2:
            print("somente 1 ou 2")
            continue

    except ValueError:
        os.system('cls')
        print("entrada invalida. digite um numero.")
        continue


    while True:
        try:            
            print('-' * 20)
            print(f'sua listas de filmes')
            print('-' * 20)
            print('[1]Ação e aventura')
            print('[2]Drama')
            print('[3]Comédia romântica')
            print('[4]Ficção científica')
            print('[5]Terror')
            print('-' * 20)

            menu2 = input('deseja entrar em qual categoria? ')
            menu2_int = int(menu2)       
            os.system('cls')

        except ValueError:
            os.system('cls')
            print("entrada invalida. digite um numero.")

        if menu2_int == 0:
            print("somente 1 ou 2")
            continue
        elif menu2_int > 5:
            print("somente de 1 a 5")
            continue


        if menu2_int == 1:
            
            print('-' * 20)
            print('Ação e aventura')
            print('-' * 20)
            
            for nome in filmes[0]:
                print(nome)

            filmeAV = input('adicionar filme: ')
            filmes[0].append(filmeAV)

            os.system('cls')
                   

        elif menu2_int == 2:
            print('-' * 20)
            print('Drama')
            print('-' * 20)

            for nome in filmes[1]:
                print(nome)

            filmeDM = input('adicionar filme: ')
            filmes[1].append(filmeDM)

            os.system('cls')


        elif menu2_int == 3:
            print('-' * 20)
            print('Comédia romântica')
            print('-' * 20)

            for nome in filmes[2]:
                print(nome)

            filmeCR = input('adicionar filme: ')
            filmes[2].append(filmeCR)

            os.system('cls')


        elif menu2_int == 4:
            print('-' * 20)
            print('Ficção científica')
            print('-' * 20)

            for nome in filmes[3]:
                print(nome)

            filmeFC = input('adicionar filme: ')
            filmes[3].append(filmeFC)

            os.system('cls')


        elif menu2_int == 5:
            print('-' * 20)
            print('Terror')
            print('-' * 20)

            for nome in filmes[4]:
                print(nome)

            filmeTR = input('adicionar filme: ')
            filmes[4].append(filmeTR)

            os.system('cls')
                