class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}.")


class Student(Person):
    pass


class Worker(Person):
    def __init__(self, age, name, job):
        # Person.__init__(self, age, name)
        super().__init__(age, name)
        self.job = job


p = Person(10, "John")
p.print_name()

s = Student(20, "Micha")
s.print_name()

w = Worker(30, "Jane", "banker")
w.print_name()
print(w.job)
print(w.age)

print(type(p))
print(type(s))
print(type(w))

