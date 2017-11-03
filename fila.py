#declarando uma fila
fila = ['Balanca', 'Vai Descendo', 'Soh', 'Da']
print 'Fila atual:',fila

#O primeiro elemento da fila sai
elemento = fila.pop(0)
print elemento,'saiu da fila'
print 'Fila atual:',fila

novo_elemento = 'Tu'
#chegou um elemento ao final da fila
fila.append(novo_elemento)
print novo_elemento,'entrou no final da fila'
print 'Fila atual:',fila

#O primeiro elemento da fila sai
elemento = fila.pop(0)
print elemento,'saiu da fila'
print 'Fila atual:',fila