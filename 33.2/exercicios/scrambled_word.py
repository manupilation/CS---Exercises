import random

PALAVRAS = [
  "mosca",
  "urubu",
  "sereia",
  "piranha",
  "dragão",
  "pirata",
  "elefante",
  "juliette",
]

MAX_ATTEMPTS = 3

def draw_secret_word(palavras):
    secret_word = random.choice(palavras)
    scrambled_word = "".join(random.sample(secret_word, len(secret_word)))
    return secret_word, scrambled_word

def collect_guesses():
    guesses = []
    for attempt in range(MAX_ATTEMPTS):
        guess = input("Guess the word: ")
        guesses.append(guess)
    return guesses

def check_game_result(secret_word, guesses):
    if secret_word in guesses:
        print(f"You win: {secret_word}")
    else:
        print(f"You lose: {secret_word}")

if __name__ == "__main__":
    secret_word, scrambled_word = draw_secret_word(PALAVRAS)
    print(f"Scrambled word is {scrambled_word}")
    guesses = collect_guesses()
    check_game_result(secret_word, guesses)