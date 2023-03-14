sair = "Sair"
while True:
    # numero1 = (float(input("Escreva o primeiro número: ")))
    # numero1 = (float(input("Escreva o segundo número: ")))
    # operador = (float(input("Digite o operador (+-*/): ")))
    numero1 = input("Escreva o primeiro número: ")
    numero2 = input("Escreva o segundo número: ")
    operador = input("Digite o operador (+-*/): ")

    
    try: #tentar executar o código
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        nmero_valido= True

    except: #caso tenha e
        numero_valido= False
    
    if numero_valido == False:
        print("Número inválido. ")
        continue
    
    operador_aceito= ("+-*/")
    
    if operador not in operador_aceito:
        print("Operador não aceito")

    sair = input ("Deseja sair? ").lower().startswith("s")
    if sair is True:
        break
    
    if operador == "+":
        print(f"{numero1_float} + {numero2} = ", numero1_float + numero2_float)
    elif operador == "-":
        print(f"{numero1_float} - {numero2} = ", numero1_float - numero2_float)
    elif operador == "*":
        print(f"{numero1_float} * {numero2} = ", numero1_float * numero2_float)
    elif operador == "/":
        print(f"{numero1_float} / {numero2} = ", numero1_float / numero2_float)
    else:
        print("Error")