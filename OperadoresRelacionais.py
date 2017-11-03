valor_1 = 5
valor_2 = 10

print valor_1 < valor_2
print valor_1 > valor_2

valor_3 = valor_1*2

print valor_1 == valor_3

valor_4 = valor_2/2

print valor_4 <= valor_1

print ((valor_1 == valor_4) == True)

idade = 0

if(idade<=0):
    print("A sua idade nao pode ser 0 ou menor do que 0!")
elif(idade>150):
    print("A sua idade nao pode ser superior a 150 ano!")
elif(idade<18):
    print("Voce precita ter mais do que 18 anos!")