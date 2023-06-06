from funcoes import limparTela, esperarSegundos, soma, lerString
limparTela()
print("Jogo da Forca! ")
esperarSegundos(3)
limparTela()
print ("Nome do Desafiante ")
nome = lerString ("Nome: ")
arquivo = open("dados.forca", "a")
arquivo.write(nome + "\n")
arquivo.close()
print("Nome Salvo")
esperarSegundos(1)
limparTela()
print ("Nome do Competidor ")
nome = lerString ("Nome: ")
arquivo = open("dados.forca", "a")
arquivo.write(nome + "\n")
arquivo.close()
print("Nome Salvo")
esperarSegundos(1)
limparTela()

print("Desafiante Informe a Palavra ")
palavra = lerString ("Palavra: ")
arquivo = open("dados.forca", "a")
arquivo.write(palavra + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
print("Desafiante Informe Dica 1 ")
dica1 = lerString ("Dica 1: ")
arquivo = open("dados.forca", "a")
arquivo.write(dica1 + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
print("Desafiante Informe Dica 2 ")
dica2 = lerString ("Dica 2: ")
arquivo = open("dados.forca", "a")
arquivo.write(dica2 + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
print("Desafiante Informe Dica 3 ")
dica3 = lerString ("Dica 3: ")
arquivo = open("dados.forca", "a")
arquivo.write(dica3 + "\n")
arquivo.close()
esperarSegundos(1)
limparTela()
while True:
   print("Quantidade de letras ↆ ") #MENU

   print("(0)Jogar")
   print("(1)Solicitar Dica")
   print("(2)Sair do Jogo")
   opcao=input()
   if opcao == "2":
    break
   elif opcao == "1":
      limparTela()
      print(dica1)
    #precisaacabar
  
   elif opcao == "0":
    if palavra:
      for x in range(100):
        print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        break
