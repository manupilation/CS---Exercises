def greaterThan(x, y):
    if(x > y):
        return x
    return y

first_question = greaterThan(6, 4)
# print(first_question)

# ====================================================================== 🦜

def arithmeticAverage(list):
    x = 0
    for number in list:
        x += number
    return x / len(list)

second_question = arithmeticAverage([1, 2, 3, 4, 5])
# print(second_question)

# ====================================================================== 🦜

def createTable(n):
    if(n > 1):
        for i in range(n):
            print(n * '*')

# third_question = createTable(160)

# ====================================================================== 🦜

def returnGreaterString(list):
    greaterString = ''
    for string in list:
        if(len(greaterString) < len(string)):
            greaterString = string
    return greaterString

fourth_question = returnGreaterString(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])
# print(fourth_question)

# ====================================================================== 🦜

def paintingCalc(meters):
    price = 80
    requiredLiters = meters / 3
    quantity = requiredLiters // 18
    if requiredLiters % 18:
        quantity += 1
    return quantity, quantity * price

fifth_question = paintingCalc(180)
# print(fifth_question)

# ====================================================================== 🦜

def typeOfTriangle(l1, l2, l3):
    typeT = 'Não é triângulo'
    if(l1 + l2 + l3 == 180):
        typeT = 'Triângulo Escaleno'
    if(l1 == l2 or l2 == l3 or l1 == l3):
        typeT = 'Triângulo Isósceles'
    if(l1 == l2 and l2 == l3):
        typeT = 'Triângulo Equilátero'
    return typeT

sixth_question = typeOfTriangle(1800, 500, 400)
sixth_question2 = typeOfTriangle(45, 45, 90)
sixth_question3 = typeOfTriangle(60, 60, 60)
sixth_question4 = typeOfTriangle(50, 40, 90)

# print(sixth_question)
# print(sixth_question2)
# print(sixth_question3)
# print(sixth_question4)