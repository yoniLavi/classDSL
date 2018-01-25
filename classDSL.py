# A silly Chef-like DSL in Python for defining school classes, inspired by Guido's
# http://python-history.blogspot.ie/2009/02/adding-support-for-user-defined-classes.html
# where he mentions:
# "Users are often surprised to learn that any sequence of valid Python
#  statements can appear in a class body."

import random


class SchoolClassMeta:
    def __new__(cls, class_name, bases, attrs, *args, **kwargs):
        students = ', '.join(attrs['students'])
        print(f'A big welcome to: {students} - our class of {class_name}')


class Aug2019(metaclass=SchoolClassMeta):
    """The students of the August class are known ahead of time"""
    students = ["Adam", "Eve"]


class Sep2019(metaclass=SchoolClassMeta):
    """For the September class, we have a free spot

    So the DSL supports writing any custom code to decide who'll take the spot
    """
    students = ["Alice", "Bob"]

    tentative_students = ["Jack", "Janice"]
    random.shuffle(tentative_students)
    size = 3
    while len(students) < size:
        students.append(tentative_students.pop())


# The above outputs the following (up to the random choice),
# without any additional code (no need to instantiate the classes):
#   A big welcome to: Adam, Eve - our class of Aug2019
#   A big welcome to: Alice, Bob, Janice - our class of Sep2019
