#-------------------------------------------------------------------------------
# Name:        Jogo da forca
# Author:      Amanda Carvalho
# 1) Ter uma lista de palavras do jogo
# 2) Selecionar uma palavra aleatória
# 3) Mostrar ao usuário um número de hífens equivalente ao número de letras da
# palavra selecionada
# 4) Repetidamente perguntar por uma letra ao usuário
# - Fazer a substituição do hífen pela letra nas posições que o usuário acertou
# - Máximo: 5 tentativas
# 5) Apresentar o resultado do jogo
#-------------------------------------------------------------------------------

palavras = ["abobora", "gato", "noite", "terror", "assustador", "fantasia", "fantasma", "zumbi", "outubro", "festa", "lobisomem", "bruxa", "aranha"]

letras_acertadas = []

letras_tentadas = []

erros = 0

max_erros = 5

import random

palavra_secreta = random.choice(palavras)

print('''Olá! Bem vindo ao jogo da forca edição de ☠ Halloween ☠! #
\n Instruções do jogo:
\n 1) Dica: as palavras do jogo estão relacionadas com a temática do Halloween;
\n 2) Você deve chutar somente UMA letra por vez, usando apenas as letras do alfabeto;
\n 3) Cada traço mostrado na tela representa uma letra da palavra; se você acertar, a letra aparecerá na posição correta;
\n 4) Você só pode errar 5 vezes! Após 5 tentativas erradas, você perde o jogo;
\n 5) Você ganhará quando descobrir a palavra oculta!
\n # Boa sorte! #''')

for x in range (len(palavra_secreta)):
    print("_", end = " ")

while erros < 5 and len(letras_acertadas) < len(palavra_secreta):

    tentativa = input("Digite uma letra: ").lower()

    if tentativa.isalpha() and len(tentativa) == 1:

        if tentativa in letras_tentadas:
            print("Você já tentou essa letra! Tente outra letra.")
        else:
            letras_tentadas.append(tentativa)

            if tentativa in palavra_secreta:
                for p in range (0, len(palavra_secreta)):
                    if palavra_secreta[p] == tentativa:
                        letras_acertadas.append(p)
            else:
                erros += 1

            for a in range (0, len(palavra_secreta)):
                if a in letras_acertadas:
                    print(palavra_secreta[a], end = " ")
                else:
                    print("_", end = " ")

            print (f"Você errou {erros} letra(s). Restam {max_erros - erros} tentativas.")
    else:
        print("Ops! Digite uma letra do alfabeto, apenas uma por vez.")

if erros == 5:
    print(f"Que pena! Você esgotou suas tentativas. A palavra era, {palavra_secreta}")
else:
    print("Parabéns, você adivinhou a palavra! :)")
