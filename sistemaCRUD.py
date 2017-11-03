import pyrebase
import os

config = {
	
	
}

firebase = pyrebase.initialize_app(config)

#pegar a referencia para autenticar o servico
auth = firebase.auth()

#pegar a referencia para o banco de dados no firebase
db = firebase.database()


condicao = True
lista_clientes = []

def cadastrar():
	print '### ------ CADASTRANDO CLIENTE ------ ###\n'
	nome = raw_input('Digite o nome do cliente: ')
	email = raw_input('Digite o email do cliente: ')
	cliente = {"nome": nome,"email":email}
	
	#Cadastrando um cliente no Firebase
	db.child("clientes").push(cliente, user['idToken'])
	os.system('cls' if os.name == 'nt' else 'clear')
	print 'Cliente: ['+nome+'] com o email ['+email+'] ADICIONADO COM SUCESSO!'


def listar():
	all_clientes = db.child("clientes").get(user['idToken'])
	#percorre os registros no databse do Firebase e exibe um por vez
	for cliente in all_clientes.each():
		nome = cliente.val()['nome']
		email = cliente.val()['email']
		print 'Cliente: ['+nome+']  | Email ['+email+']'

def editar():
	print '### ------ EDITANDO CLIENTE ------ ###\n'
	listar()
	all_clientes = db.child("clientes").get(user['idToken'])

	cliente_edicao = raw_input('DIGITE O NOME DO CLIENTE QUE DESEJA EDITAR: ')
	print '[0] - EDITAR NOME\n'+'[1] - EDITAR EMAIL\n'
	comando = input('DIGITE SUA OPCAO PARA EDITAR: ')

	if(comando == 0):
		#percorre os registros no databse do Firebase e exibe um por vez
		for cliente in all_clientes.each():	
			if(cliente_edicao == cliente.val()['nome']):
				novo_nome = raw_input('DIGITE O NOVO NOME DO CLIENTE: ')
				db.child("clientes").child(cliente.key()).update({"nome": novo_nome},user['idToken'])
				os.system('cls' if os.name == 'nt' else 'clear')
				print 'EDICAO REALIZADO COM SUCESSO!'
	elif(comando == 1):
		#percorre os registros no databse do Firebase e exibe um por vez
		for cliente in all_clientes.each():	
			if(cliente_edicao == cliente.val()['nome']):
				novo_email = raw_input('DIGITE O NOVO EMAIL DO CLIENTE: ')
				db.child("clientes").child(cliente.key()).update({"email": novo_email},user['idToken'])
				os.system('cls' if os.name == 'nt' else 'clear')
				print 'EDICAO REALIZADO COM SUCESSO!'		
	else:
		print 'COMANDO INVALIDO!'

def remover():
	print '### ------ REMOVENDO CLIENTE ------ ###\n'
	listar()
	all_clientes = db.child("clientes").get(user['idToken'])
	cliente_remocao = raw_input('DIGITE O NOME DO CLIENTE QUE DESEJA REMOVER: ')

	for cliente in all_clientes.each():
		if(cliente_remocao == cliente.val()['nome']):
			print 'CONFIRMAR REMOCAO DO CLIENTE ['+cliente_remocao+']\n'+'[0] - SIM\n'+'[1] - NAO\n'
			comando_remocao = input('DIGITE UMA OPCAO: ')
			if(comando_remocao == 0):
				db.child("clientes").child(cliente.key()).remove(user['idToken'])
				os.system('cls' if os.name == 'nt' else 'clear')
				print 'OPERACAO DE REMOCAO REALIZADA COM SUCESSO!'
			elif(comando_remocao == 1):
				os.system('cls' if os.name == 'nt' else 'clear')
				print 'OPERACAO DE REMOCAO CANCELADA!'
			else:
				print 'COMANDO INVALIDO!'

print '### ------ LOGIN ------ ###\n'
email = raw_input('DIGITE SEU EMAIL: ')
password = input('DIGITE SUA SENHA: ')
os.system('cls' if os.name == 'nt' else 'clear')
print '### ------ USUARIO AUTENTICADO COM SUCESSO! ------ ###\n'

#logar o usuario pelo email e senha previamente fornecido
user = auth.sign_in_with_email_and_password('felipe.sa.oliveirati@gmail.com', 123456)

while (condicao == True):
	print '### ------ MENU SECOMP 2017 ------ ###\n'
	print '[0] - Cadastrar Cliente\n'+'[1] - Listar Clientes\n'+'[2] - Editar Cliente\n'+'[3] - Remover Cliente\n'+'[4] - Sair'
	comando = input('DIGITE UMA OPCAO: ')
	
	if(comando == 0):
		os.system('cls' if os.name == 'nt' else 'clear')
		cadastrar()
	elif(comando == 1):
		os.system('cls' if os.name == 'nt' else 'clear')
		print '### ------ LISTAR CLIENTE ------ ###\n'
		listar()
	elif(comando == 2):
		os.system('cls' if os.name == 'nt' else 'clear')
		editar()
	elif(comando == 3):
		os.system('cls' if os.name == 'nt' else 'clear')
		remover()
	elif(comando == 4):
		print 'O programa vai parar agora!'
		condicao = False
	else:
		print 'Comando Invalido!',comando