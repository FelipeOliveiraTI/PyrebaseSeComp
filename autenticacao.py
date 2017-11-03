import pyrebase

config = {
	
	#Suas configuracoes aqui
}

firebase = pyrebase.initialize_app(config)

#pegar a referencia para autenticar o servico
auth = firebase.auth()

#logar o usuario pelo email e senha previamente fornecido
user = auth.sign_in_with_email_and_password('felipe.sa.oliveirati@gmail.com', 123456)

#pegar a referencia para o banco de dados no firebase
db = firebase.database()

data = db.child("clientes").get(user['idToken'])
print(data.val())