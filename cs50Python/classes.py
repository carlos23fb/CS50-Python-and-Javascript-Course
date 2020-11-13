# class Point():
#     """
#     docstring
#     """

#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2


# p = Point(2, 8)
# print(p.x)
# print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)


people = ["Harry", "Ron", "Hermaione", "Snape"]

flight = Flight(3)

for person in people:
    if flight.add_passanger(person):
        print(f"{person} has a seat")
    else:
        print(f"{person} dont have a seat, flight already out of capacity")
