from unicodedata import name


people = [
  {"name":"Harry", "house":"Gryffindor"},
  {"name":"Cho", "house":"Ravenclaw"},
  {"name":"Draco", "house":"Slytherin"}
]

def f(person):
  return person["house"]

#TypeError: '<' not supported between instances of 'dict' and 'dict'
people.sort(key=f)

people.sort(key=lambda person: person["name"])

print(people)
