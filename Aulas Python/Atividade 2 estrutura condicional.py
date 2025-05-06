# #Verificação de número par ou ímpar
# # if significa se / % resto / else = se não / elif = se não se

# numero = int(input("Digite um numero : "))
# #and significa E / ! = diferente / or significa ou
# if numero % 2 == 0 and numero != 0:
#    print("é par")

# elif numero % 2 == 1 :
#     print("é ímpar")

# else:
#     print("o numero é zero")


# #Solicite dois numeros e determine qual deles é maior
# #Solicite dois numeros
# numero1 = int(input("Digite o numero 1: "))
# numero2 = int(input("Digite o numero 2: "))
# #determine qual deles é maior
# if numero1 > numero2:
#    print("o numero 1 é o maior") 
# elif numero2 > numero1:
#      print("o numero 2 é maior")
# #else não tem condição
# else:
#     print("os numeros são iguais")     
# #Mostre o resultado    

# #Verificação de Idade para Dirigir
# #Peça a idade do usuário
# Idade = int(input("Digite a Idade: "))
# # verifique se ele tem idade suficiente > 18
# if Idade > 18:
#    print("Pode Dirigir")

# elif Idade < 18:
#      print("Não pode dirigir") 

# else:
#     print("Idade para dirigir")
# #mostre o resultado

        
# #Verificação de número positivo, negativo ou zero
# Numero = int(input("Digite o Número:"))
# #Determine se um numero é positivo
# if Numero > 0:
#     print("positivo")
 
# #Determine se um numero é negativo
# elif Numero < 0:
#     print("negativo") 

# #Determine se um numero é zero
# else:
#     print("O numero é zero"


# #Peça ao usuário os comprimentos dos três lados de um triangulo e determine se é equilatero, isosceles ou escaleno
# lado1 = int(input("Digite o lado do triangulo:"))
# lado2 = int(input("Digite o lado do triangulo: "))
# lado3 = int(input("Digite o lado do triangulo"))

# if lado1 == lado2 == lado3:
#    print(" Esté trinagulo é equilatero")

# #!= diferente
# elif lado1 != lado2 != lado3 and lado1 != lado3:
#      print("Esse é o triangulo escaleno")

# else: 
#     print("É o triangulo isosceles") 

#Outra maneira de fazer
# if lado1 == lado2 == and lado2 == lado3:
#     print(equilatero)
# 
# elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3
#      print (é isosceles)    

#else:
#    print("é escaleno")
 
# #Solicite ao usuario para digitar uma letra

# letra = input("Digite uma letra:")


# #determine se é uma vogal
# if letra =="a" or letra =="e" or letra == "i" or letra == "o" or letra == "u":
#     print("É uma vogal")

# #ou uma consoante
# else:
#     print("É uma consoante")   
# 

# #Solicite a nota do aluno em uma disciplina e determine se ele foi aprovado (nota maior ou igual a 7) ou reprovado
# Nota = int(input("Digite a nota: "))

# if Nota >= 7:
#     print("Aluno aprovado")

# else: 
#      print("Aluno reprovado")


# #Peça ao usuario para digitar um numero e verifique se é divisivel por 3 e 5 ao mesmo tempo
# Numero = int(input("Digite um numero: "))

# if Numero % 3 == 0 and Numero % 5 == 0:
#          print("é divisivel por 3 e 5")

# else:
#      print("não é divisivel por 3 e 5")

#Cálculo de Desconto com condição
#Peça ao usuario o valor de um produto e calcule o valor em desconto apenas se o valor original for maior que $100
Valor = int(input("Digite o valor de um produto: "))





#Solicite a idade do usuario e classifique-a em Criança, Adolescente, Adulto Jovem ou Adulto
Idade = int(input("Digite a idade: "))

if Idade < 12:
    print("É uma criança")

elif Idade >= 12 and Idade < 18:
    print(" É um adolescente")


else Idade > 18
     print(" É adulto jovem ou Adulto")
   
