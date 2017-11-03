#declarando uma lista vazia
lista = []

#Adicionar elementos
lista.append('Joelma')
lista.append('Chimbinha')
lista.append('Safadao')
lista.append('Annita')
print lista

#inserir elemento em uma posicao especifica
lista.insert(0,'Mc Troinha')
print lista

#remover um elemento pelo valor
lista.remove('Annita')
print lista

#pegando posicao do elemento pelo valor
local = lista.index('Safadao')
print local

#removendo um elemento pelo index
del(lista[local])
print lista

#invertendo ordem da lista
lista.reverse()
print lista

#ordenando uma lista
lista.sort()
print lista

