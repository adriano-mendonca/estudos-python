text = str(input('Digite um frase:')).strip().upper()
print(f'A letra "a" aparece {text.count("A")} vezes.')
print(f'A primeira vez que a leta "a" aparece na sua frase é na {text.find("A")+1}° posição.')
print(f'A última vez que a letra "a" aparece na sua frase é na {text.rfind("A") +1}° posição.')
