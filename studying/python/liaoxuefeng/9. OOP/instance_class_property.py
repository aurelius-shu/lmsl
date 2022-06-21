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
    print(s.count)
    print(Student.count)
    print('--------------------------')
    s2 = Student('Aurelius2')
    print(s2.name)
    print(Student.name)
    print(s2.count)
    print(Student.count)
    print('--------------------------')
    s.name = 'Aurelius.Shu'
    print(s.name)
    print(s2.name)
    print(Student.name)
    print('--------------------------')
    del s.name
    print(s.name)
