class Student(object):
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


class StudentA(Student):
    # __slots__ = ('score', 'a')
    pass


class StudentB(Student):
    __slots__ = ('score', 'a')


if __name__ == "__main__":
    a = Student('Aurelius', 18)
    print(a.name, a.age)
    b = StudentB('Aurelius', 18)
    b.score = 100
    print(b.name, b.age, b.score)
    b.scores = [99, 100]
    print(b.scores)