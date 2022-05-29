a = 10
b = 5
print (a + b)

# =========================================================

hours = 6
minutes = hours * 60
seconds = minutes * 60
print(hours ,minutes, seconds)

# =========================================================

capa = 24.20
desconto = 0.40
primeiroEx = 3
restantesEx = 0.75

finalValue = ((capa * 60 * desconto) + primeiroEx + (restantesEx * 59))
print (finalValue)

# =========================================================

trybe_course = ["Introdução", "Front-end", "Back-end"]

trybe_course.append("Ciência da computação")
trybe_course[0] = "Fundamentos"
print(trybe_course)

# =========================================================

var = set()
var.add("Manu")

print(var)

info = {
  "personagem": "Margarida",
  "origem": "Pato Donald",
  "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}

info["recorrente"] = "sim"
del info["origem"]

print(info)

# =========================================================

initialNumber = 5
counter = 1
result = 1

while counter <= initialNumber:
    result = result * counter
    counter += 1

print(result)

# =========================================================

ratings = [6, 8, 5, 9, 10]

finalEvaluation = [x * 10 for x in ratings]

print(finalEvaluation)


# =========================================================


for rating in ratings:
    if (rating % 3) == 0:
        print(f'{rating} é multiplo de 3!')
