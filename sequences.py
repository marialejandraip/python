name = "Aleja"
print(name[1])
#Define a list of names 
#store elements in order will be better a list
names = ["Maria", "Felipe", "Ana"]
print(names[1])

names.append("Andrea")
print(names)

names.sort()
print(names)

#Create an empty set
s= set()

#Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(s)

s.remove(4)
print(s)
print(len(s))