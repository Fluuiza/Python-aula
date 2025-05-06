# #Soma de dois numeros
# Num1 = int(input("Digite o primeiro numero: "))
# Num2 = int(input("Digite o segundo numero: "))
# resultado = Num1 + Num2
# print("O resultado é: ", resultado)

# #Média de três notas
# nota1 = int(input("Digite a primeira nota: "))
# nota2 = int(input("Digite a segunda nota: "))
# nota3 = int(input("Digite a terceira nota: "))
# #calcule a média delas.
# resultado = (nota1 + nota2 + nota3) / 3
# #mostrar resultado
# print("A mmédia das notas é: ", resultado)

# #Conversão de Temperatura
# Temperaturacelsius = int(input("Temperatura celsius: "))
# resultado = (Temperaturacelsius * 9 / 5) + 32
# print("Temperaturacelsius é: " , resultado)

# #Calculo de área de um retangulo A = b.h
# Largura = int(input("Digite Largura do Retângulo: "))
# Altura = int(input("Digite Altura do Retângulo: "))
# resultado = (Largura * Altura)
# print("Calculo da área do retângulo é:" , resultado)

# #Cálculo IMC
# Peso = float(input("Digite o peso em KG: "))
# Altura = float(input("Digite a altura em M: "))
# resultado = Peso / (Altura * Altura) 
# print("O IMC é: " , resultado)

# #Cálculo de Desconto
# Produto = int(input("Valor do Produto: "))
# Desconto = int(input("Porcentagem do Produto: "))
# Resultado = (Produto * Desconto) / 100
# Final = Produto - Resultado
# print("O valor do produto com desconto é: " , Final)

#Calculadora de Juros Simples J = C x i x t (Juros, capital, taxa de juros e tempo da aplicação)
# Principal = int(input("Valor Principal: "))
# Taxa = int(input("Valor da Taxa: "))
# Anos = int(input("Valor de Anos: "))
# Montante = (Principal * Taxa * Anos) / 100
# Resultado = Montante + Principal
# print("O resultado é: ", Resultado)


# #Conversão de Idade
# Idade = int(input("Digite Idade em Anos: "))
# Meses = Idade * 12
# Dias = Idade * 365
# print("O resultado é:", Dias )
# print ("O resultado em meses é:", Meses)

# #Troca de Valores
# Valor1 = int(input("Digite o primeiro valor: "))
# Valor2 = int(input("Digite o segundo valor: "))
# Valor3 = Valor2
# Valor2 = Valor1
# Valor1 = Valor3
# print("O primeiro valor é : ", Valor1)
# print("O segundo do valor é : ", Valor2)


#Média Ponderada
Nota1 = int(input("Digite as nota 1: "))
Nota2 = int(input("Digite as nota 2: "))
Nota3 = int(input("Digite as nota 3: "))
Peso1 = int(input("Digite os peso 1: "))
Peso2 = int(input("Digite os peso 2: "))
Peso3 = int(input("Digite os peso 3: "))
Calculo = ((Nota1 * Peso1) + (Nota2 * Peso2) + (Nota3 * Peso3))/ (Peso1+Peso2+Peso3)
print("O resultado da média ponderada é: " , Calculo)