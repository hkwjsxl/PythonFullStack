class School:
    def __init__(self, name, class_obj):
        self.name = name
        self.class_obj = class_obj
        self.class_list = []

    def add_class(self):
        self.class_list.append(self.class_obj)
        return self


class Classes:
    def __init__(self, name, stu_obj):
        self.name = name
        self.stu_obj = stu_obj
        self.stu_list = []

    def add_stu(self):
        self.stu_list.append(self.stu_obj)
        return self


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def run():
    stu1 = Student('hkw', 18)
    stu2 = Student('jon', 20)

    cla1 = Classes('Python', stu1)
    cla2 = Classes('Linux', stu2)

    school1 = School('ks', cla1)
    school2 = School('bd', cla2)

    print(school1.class_obj.stu_obj.name)
    print(school2.class_obj.stu_obj.name)


if __name__ == '__main__':
    run()
