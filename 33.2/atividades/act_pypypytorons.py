# Boas-vindas novamente, pitão <3 🦜🦜🦜🦜🦜🦜
import random

random_number = random.randint(1, 12)
guess = ''

while guess != random_number:
    guess = int(input("Adivinhe o número sorteado entre 1 e 12 e ganhe um passarinho do título!"))

print('Parabens, tome seu passarinho 🦜!. O número era: ', guess)
