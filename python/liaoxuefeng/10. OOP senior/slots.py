class Student(object):
    __slots__ = ('name')

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    s = Student('Aurelius', 18)
    print(s.name, s.age)