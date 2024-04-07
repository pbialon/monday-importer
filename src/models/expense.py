from models.people import Person
from pendulum import pendulum
from typing import Map


class Expense:
    def __init__(self, name, date: pendulum.datetime, amount: float, who_paid: Person, split_between: Map[Person, float]) -> None:
        self.name = name
        self.date = date
        self.amount = amount
        self.who_paid = who_paid
        self.split_between = split_between

    def __str__(self) -> str:
        return f'{self.name} {self.date} {self.amount} {self.who_paid} {self.split_between}'