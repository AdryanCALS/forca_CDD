palavra = ["E", "X", "C", "E", "T", "O"]
#array com as imagens do jogo da forca, fonte: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
#adicionar função que quando o usuario digita a palavra toda, funciona
#poder alterar o tamanho das palavras
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
erros = 1
indice_forca = 0
resultado = "Voce Perdeu!!"
guess = input("Digite uma letra: ").upper()#usei o metodo upper para deixar todas as letras digitadas pelo usuário maíusculas
letras_usadas = []
acertos = ["_"]*len(palavra)

while erros < 6: 
    
    #imprimindo as letras que já foram usadas pelo usuario
    letras_usadas.append(guess)
    print(f"\nLetras usadas: {letras_usadas}\n")
    
    #verificando se a letra esta ou nao na palavra
    if guess in palavra:
        
        #vendo em qual posição o item esta na lista, baseado no exercicio da aula de 29/04 
        for i in range(len(palavra)):
            if palavra[i] == guess:
                #palavra[i] = "_"#nao usar remove pois ele altera o tamanho da lista e da erro: index out of range
                acertos[i] = guess
   
        print(f"Letras acertadas: {acertos}")
        
        
        print("Acertou")
        print(HANGMANPICS[indice_forca])
        #verifica se voce acertou a palavra
        if acertos == palavra:
            resultado = "Voce venceu!!"
            break
        
        guess = input("Digite uma letra: ").upper()#usei o metodo upper para deixar todas as letras digitadas pelo usuário maíusculas
        
       
    else:
        indice_forca +=1
        print(f"Letras acertadas: {acertos}")
        print(HANGMANPICS[indice_forca])
        guess = input("Digite uma letra: ").upper()#usei o metodo upper para deixar todas as letras digitadas pelo usuário maíusculas
        erros+=1
        
if resultado != "Voce venceu!!":
    indice_forca+=1
    
print(HANGMANPICS[indice_forca])
print(resultado)
