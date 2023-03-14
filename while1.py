sistema = True #cria o dado boleano

while sistema:
    nome = input ("Escreva o seu nome: ") #cria o dado que recebe um input que vai receber um valor em string
    print (f"O nome recebido foi: {nome}") #Exibe o nome

    if nome == "Sair":
        print("Finalizou o sistema")
        break