a = 10
b = 3.5
name = "SALAVARRIA"
is_active = True

print(a, b, name, is_active)

print(type(a))
print(type(name))
print(type(is_active))

device = "router"
id = 101

print(f"Device: {device} and ID: {id}")

# API
numbera = 2
numberb = 3

print("The result of adding two numbers is: ", numbera + numberb)
print("The result of subtraction is: ", numbera - numberb)
print("The result of multiplication is: ", numbera * numberb)
print("The result of power to any number is: ", numbera ** numberb)
print("The result of division is: ", numbera / numberb)
print("The result of floor division is: ", numbera // numberb)

# STRINGS
print("STRING")
name = "juanita loor"
print(name.upper())
print(name.capitalize())
name2 = name.upper()
print(name2.lower())

# INDEXING
language = 'PYTHON'
print(language[0])
print(language[-1])
print(len(language))

#LIST
print("#LIST")
devices=['router','switch',"cable",45,True,False]
print(len(devices))

print(devices[0])
print(devices[-1])

devices.append('Server')
print(devices)

names=list()
names.append('JUANITA')
names.append('ISA')
names.append('LIAM')
names.append('EITHAN')
print(names)
names[1]='DEI'
print(names)

print(names.pop())
print(names)


#Lista number
print('#LISTA number')
numbers= list(range(10))
print(numbers)
selectednumbers=numbers[2:4]
print(selectednumbers)
print(numbers[:-1])
print(numbers[:3])
numbers[2:3]=[100,100]
print(numbers)


print('#Tuples')

containertuple = (10, 20, 30, 40)

print(containertuple[0])
print(containertuple[-1])
print(len(containertuple))

containerlist = list(containertuple)
print(type(containerlist))
print(containerlist)


#DICTIONARY
print('#DICTIONARY')
animals={'dog':'nice','cat':'pretty','monkey':'black'}

print(animals['cat'])

animals['cat']='ugly'
print(animals)


print('Turtle'in animals)


del animals ['monkey']
print(animals)

animals['monkey']='ugly'
animals['nouse']='ugly'
animals['donkey']='big'


for item in animals
    facture=animals[item]
    print("%item has %feature")
print('OK')