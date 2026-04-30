Word = input('Digite uma palavra: ')
CapslockWord = Word.upper()
InverWord = CapslockWord[::-1]


if CapslockWord == InverWord:
    print(f'{Word} é um palindromo')
else:
    print(f'{Word} não é um palindromo')

#Falta remover espaços vazios de frases e simbolos como , . \