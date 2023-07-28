class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(__name__)  
        return True 
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)
people = ["Harry", "Hermione", "Ron", "Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Addes {person} to flight successfully")
    else:
        print(f"No available seats for {person}")

