import json
import random

f = open("words.json", encoding= "utf8")

words = json.load(f)
choiceComputer = random.choice(list(words.keys()))

print('Olá, seja bem-vindo!\n')

numberChoices = 5
win = False

while numberChoices > 0 and win is not True:
    print('A dica é: ' + words[choiceComputer])
    answerUser = input("Data: DDMMAAA\n")

    if len(answerUser) != 8:
        print('Erro. A resposta deve conter até 8 digitos.')
        continue

    if answerUser.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answerUser[i] == choiceComputer[i]:
                check.append("✅")
                pontuation = pontuation + 1
            else:
                check.append("❌")

        print("Resposta:\n")
        print("|".join(check))
        print(" |".join(answerUser))

        if pontuation == 8:
            win = True
    else:
        print("A resposta deve ser uma data!")
        continue
    numberChoices = numberChoices -1

if win == True:
    print('Você venceu!') 
else:
    print('Você perdeu!')
    print('A resposta era: ' + choiceComputer)      