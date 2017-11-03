#declarando um dicionario com alguns elementos (Chave:valor)
dic_pernambucano = {'Sport':41,'Santa Cruz':29,'Nautico':21}

#adicionando um elemento ao dicionario (Chave:valor)
dic_pernambucano['Salgueiro'] = 0
print dic_pernambucano

#buscando um valor com base na chave
quant_titulos = dic_pernambucano.get('Sport')
print 'O Sport tem',quant_titulos,'titulos'

#remover um elemento com base na chave
del dic_pernambucano['Salgueiro']
print dic_pernambucano

#remove a chave e retorna seu valor
valor = dic_pernambucano.pop('Nautico')
print 'O valor retornado da chave Nautico eh:',valor
print dic_pernambucano

#verificar se uma chave existe no dicionario
print 'Santa Cruz' in dic_pernambucano

#pegar todas as chaves do dicionario
print dic_pernambucano.keys()

#pegar todos os valores do dicionario
print dic_pernambucano.values()

