class Employee:
    def __init__(self, id_num, name):
        self.id = id_num
        self.name = name

    @property
    def data(self):
        return {"id": self.id, "nome": self.name}

class Hashmap:
    def __init__(self):
        self._buckets = [None for i in range(10)]

    def get_adress(self, id):
        return id % 10

    def insert(self, employee):
        address = self.get_adress(employee["id"])
        self._buckets[address] = employee

    def get_value(self, id_num):
        address = self.get_adress(id_num)
        return self._buckets[address].name

    def has(self, id_num):
        address = self.get_adress(id_num)
        return self._buckets[address] is not None

    def see_bucket(self):
        return self._buckets

    def update_value(self, id_num, new_name):
        address = self.get_adress(id_num)
        self._buckets[address]["nome"] = new_name


class Register:
    def __init__(self, list_of_employess):
        self.hash = Hashmap()
        for id_num, emp in list_of_employess:
            employee = Employee(id_num, emp)
            self.hash.insert(employee.data)


employees = [(14, "Márcia"), (23, "Jaque"), (10, "Lanai"), (9, "Carlos"), (88, "Pova")]
reg = Register(employees)
reg.hash.update_value(14, "Matheus")
print(reg.hash.see_bucket())