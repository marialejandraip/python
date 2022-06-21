#methods and objects

class Point():
  def __init__(self, x, y) -> None:
      self.x = x
      self.y = y

p = Point(2,8)
print(p.x)
print(p.y)

class Flight():
  def __init__(self, capacity, ) -> None:
      self.capacity = capacity
      self.passengers = []
  
  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True
  
  def open_seats(self):
    return self.capacity - len(self.passengers)

flight = Flight(3)

names = ["Maria", "Felipe", "Ana", "Andrea"]
for person in names:
  success = flight.add_passenger(person)
  if success:
    print(f"Added {person} to flight successfully")
  else:
    print(f"No seats available for {person} to the flight")
