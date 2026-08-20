class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        return amount + amount * 0.10


b1 = Bus("AIUB Bus", 40)

print("Bus Name:", b1.name)
print("Seating Capacity:", b1.seating_capacity)
print("Total Fare:", b1.fare())