#aluna Maria Clara Fonseca de Vasconcelos

#q1
for _ in range(20):
    print("Eu estou aprendendo a escrever programas de computador! É muito empolgante!")

#q2
for i in range(1, 21, 2):
    print(i)

#q3
soma = sum(range(1, 11))
print("A soma dos números de 1 a 10 é:", soma)

#q4
numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(10)]
media = sum(numeros) / len(numeros)
print("A média aritmética é:", media)

#q5
maiores_de_idade = 0
for i in range(20):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    if idade >= 18:
        maiores_de_idade += 1
print("Quantidade de pessoas maiores de idade:", maiores_de_idade)

#q6
menor = float('inf')
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < menor:
        menor = numero
print("O menor número digitado foi:", menor)

#q7
for i in range(15):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
        print(numero)

#q8
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


#q9
nomes = []
idades = []
for i in range(10):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    nomes.append(nome)
    idades.append(idade)

mais_velha = nomes[idades.index(max(idades))]
mais_nova = nomes[idades.index(min(idades))]
media_idade = sum(idades) / len(idades)

print("Pessoa mais velha:", mais_velha)
print("Pessoa mais nova:", mais_nova)
print("Média das idades:", media_idade)

#q10
votos = [0, 0]  # votos[0] para o candidato 1 e votos[1] para o candidato 2
for i in range(10):
    voto = int(input(f"Eleitor {i+1}, digite 1 para o candidato 1 ou 2 para o candidato 2: "))
    if voto == 1:
        votos[0] += 1
    elif voto == 2:
        votos[1] += 1

if votos[0] > votos[1]:
    print("Candidato 1 ganhou a eleição!")
elif votos[1] > votos[0]:
    print("Candidato 2 ganhou a eleição!")
else:
    print("Houve um empate!")

#q11
salario_minimo = 850
abaixo_minimo = 0
for i in range(5):
    salario = float(input(f"Digite o salário da {i+1}ª pessoa: "))
    if salario < salario_minimo:
        abaixo_minimo += 1
print("Quantidade de pessoas com salário abaixo do mínimo:", abaixo_minimo)

#q12
quantidade = int(input("Digite a quantidade de números pares que deseja exibir: "))
numero = 2
for _ in range(quantidade):
    print(numero, end=" ")
    numero += 2
print()
