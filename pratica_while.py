condicao = True

while (condicao == True):
	comando = raw_input('Foceca um comando: ')
	if(comando == 'parar'):
		print 'O programa vai parar agora!'
		condicao = False
	else:
		print 'voce digitou o comando',comando