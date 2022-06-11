LIST_TO_TEST = [12, 10, 9, 2, 15]

def fizz_buzz(list_of_numbers):
    final_list = list()
    for number in list_of_numbers:
        if number % 3 == 0 and number % 5 == 0:
            final_list.append('FizzBuzz')
        elif number % 3 == 0:
            final_list.append('Fizz')
        elif number % 5 == 0:
            final_list.append('Buzz')
        else:
            final_list.append(number)
    return final_list

final_result = fizz_buzz(LIST_TO_TEST)
print(final_result)