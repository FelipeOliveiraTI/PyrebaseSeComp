conta = 0
#laco que roda ate condicao ser satisfeita
while(conta <= 10):
    conta += 1
    print(conta)

#laco que executa condicao quando for True e altera pra false
condicao = True
while(condicao):
    print("BLOCO while() e condicao==True")
    condicao = False
else:
    print("BLOCO ELSE e condicao==False")

#laco invocando o comando Break
condicao = True
while(condicao):
    print("BLOCO while() e condicao==True")
    condicao = False
    break
else:
    print("BLOCO ELSE e condicao==False")    