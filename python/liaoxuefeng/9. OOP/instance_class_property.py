class Student(object):
    count = 0
    name = 'Student'

    def __init__(self, name):
        self.name = name
        Student.count += 1


if __name__ == "__main__":
    s = Student('Aurelius')
    print(s.name)
    print(Student.name)
    s.name = 'Aurelius.Shu'
    print(s.name)
    print(Student.name)
    del s.name
    print(s.name)
