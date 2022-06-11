numbers = input('Digite dois ou mais números separados por um espaço🦜🦜🦜🦜: ')

separe_numbers = numbers.split()

valid_numbers = []

for num in separe_numbers:
    if num.isdigit():
        valid_numbers.append(int(num))
    else:
        print('ERROOOOOOO: invalid number 😠😠😠')


print(sum(valid_numbers))
