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

data = {'Nome': 'Felipe Oliveira'}
#Enviando por push o firebase cria um id automatico
db.child("users").push(data, user['idToken'])

#Enviando por set podemos fonecer um id para cada user
#por exemplo enviamos o id "Gerente" para o user
db.child("users").child('Gerente').set(data, user['idToken'])

#MULTI SAVE
#exemplo de um modelo de dados que vamos armazenar
data = [{"Nome": "MC Troinha",
		"Idade": 26,
		"Sexo": "Masculino",
		"Status": "Cantor de Sucesso"},
		{"Nome": "Safadao",
		"Idade": 32,
		"Sexo": "Masculino",
		"Status": "Rico e bem novinho"}
		]

#percorrendo a lista para pegar nome e valores para enviar por set
for elemento in data:
	nome = elemento['Nome']
	db.child("Artistas").child(nome).set(elemento, user['idToken'])

#UPDATE
db.child("Artistas").child("Safadao").update({"Nome": "Wesley"},user['idToken'])

#MULTI UPDATE
#declarando novos dados
data = {
    "Artistas/MC Troinha/": {
        "Status": "No mundo"
    },
    "Artistas/Safadao/": {
        "Status": "Rico"
    }
}

#chamando funcao para realizar a alteracao
db.update(data,user['idToken'])

#REMOVE
db.child("Artistas").child("Safadao").remove(user['idToken'])


#RETRIEVE
#.val()
#Armazena na variavel 'data' os dados que estao no Firebase
data = db.child("Artistas").get(user['idToken'])
print(data.val())

#.ket()
#Armazena na variavel data os dados que estao no Firebase
data = db.child("Artistas").get(user['idToken'])
print(data.key())

#.each()
#Pega todos os registros no banco
all_artistas = db.child("Artistas").get(user['idToken'])
#percorre os registros e exibe cada um
for artista in all_artistas.each():
    print(artista.key()) 
    print(artista.val())

#.shallow().
#Armazena na variavel data os dados que estao no Firebase
all_artistas_ids = db.child("Artistas").shallow().get(user['idToken'])
print(all_artistas_ids.key())


#STORAGE
#Cria uma referencia para o compente de storage no Firebase
storage = firebase.storage()

#.put()
#Enviar para o Storage a imagem do amigo Zeca
results = storage.child("images/example.jpg").put("zeca.jpg")

#.download()
#Enviar para o Storage a imagem do amigo Zeca
storage.child("images/example.jpg").download("download/zeca_down.jpg")