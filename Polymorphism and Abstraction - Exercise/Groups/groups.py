from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)


class Group(Person):
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(name=f"{self.name} {other.name}", people=self.people + other.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(repr(x) for x in self.people)}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"