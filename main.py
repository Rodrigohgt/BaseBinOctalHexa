#Grupo: #Alvaro Alves Araujo/RGM:30040124
        #Kleber Moura Bezerra/RGM:29366488
        #Raquel de Lima Souza/RGM:25158201      
        #Rodrigo Henrique G Teixeira/RGM:7224821985
        #Samuel Sampaio da Silva/RGM:28977688

#Projeto interdisciplinar: conversor de bases numéricas
#Primeiro atraves do loop o usuario entra com a opção de conversão de decimal, para a outra base desejada(1 binária, 2 octal, 3 hexadecimal))

loop = True

#enquanto o loop for verdadeira o codigo sera executado
while loop:
    print( '''opções:
    [1] Base Binária
    [2] Base Octal
    [3] Base Hexadecimal
    [4] Digite um novo valor
    [5] Finalizar Conversões''')
    base = int(input("Digite qual base você gastaria de escolher: "))

#Na primeira estrutura de repetição, caso o usuario digite o valor de 1, sera executado o algortimo abaixo
    if base == 1:
        n = int(input("Digite o valor decimal que gostaria de converter: "))
        k = []
        #enquanto n maior que 0, o calculo sera executado.
        while (n > 0):
            a = int(float(n%2))
            k.append(a)
            n = (n - a)/2
        k.append(0)
        string=""
        for j in k[::-1]:
            string=string+str(j)
        print(string)
        break

#Na segunda estrutura de repetição, caso o usuario digite o valor de 2, sera executado o algortimo abaixo 
    elif base == 2:
        n = int(input("Digite o valor decimal que gostaria de converter: "))
        string = " "
        #enquanto n maior que 0, o calculo sera executado.
        while n > 0:
            remainder = n % 8
            n = n // 8
            string = str(remainder) + string
        print(string)
        break

#Na terceira  estrutura de repetição, caso o usuario digite o valor de 3, sera executado o algortimo abaixo
    elif base == 3:
        n = int(input("Digite o valor decimal que gostaria de converter: "))
        he = ''
        #Dicionario de base de conversão.
        dic =  { 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 
        8.: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: "F"}
        
        while(n != 0):
            c = n%16
            he = dic[c] + he
            n = int (n/16)

        print(he)

        break

#Na quarta estrutura de repetição, caso o usuario digite o valor de 4, sera executado o algortimo abaixo
    elif base == 4:
        print("Digite um novo valor")
        continue

#Na quinta estrutura de repetição, caso o usuario digite o valor de 5, sera executado o algortimo abaixo
    elif base == 5:
        print("Finalizando")
        break
#e caso e digite qualquer outro valor que sera diferente ele volta para o loop
    else:
        print("tente novamente")
        continue