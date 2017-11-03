nome_aluno = 'Chimbinha'
nota_1 = 3
nota_2 = 2

media = (nota_1 + nota_2)/2

#verifica se aluno teve media maior igual a 7 ou menos que 10
if(media >= 7 and media <=10):
	print nome_aluno,'foi aprovado com a media',media
#verifica se o aluno teve media entre 3 e 7
elif(media >=3 and media <7):
	print nome_aluno,'esta na recuperacao com media',media
	#verifica se o aluno teve media menor que 3 e maior ou igual a 0
elif(media<3 and media>=0):
	print nome_aluno,'foi reprovado com media',media
else:
	print 'valores impossiveis!'



