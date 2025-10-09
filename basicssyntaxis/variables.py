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

#tuple
print('#Tuples')
containertuple = (10, 20)
print(containertuple[0])

containerlist = list(containertuple)


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


for item, feature in animals.items():
   print(f"{item} has {feature}")



mydictionary=dict()
mydictionary['humans']=2
mydictionary['mause']=4
mydictionary['spider']=8

for animal in mydictionary:
    data=mydictionary[animal]
    print('the %s has %d'%(animal,data))

#LOOPS
counter=0
while counter<10:
    print(counter)
    counter=counter+1
    #counter+=1
#name=input('Enter your name: \n')
#print(f'Hello, {name}')

myList=list()
for i in range(10):
    if i%2==0:
        myList.append(i)

print(myList)

print('---------------')
myList=[ i for i in range(10) if i%2==0]
print(myList)

print('---------------')
myList=[i*i for i in range(100)]
print(myList)

print('OK')


def greetings():
    return f'Hello my friend...'

tmp=greetings()
print(tmp)

def greetings2(name):
    print(f'Hello, {name}')
    return
#greetings2('JUANITA')
greetings2()
print('---------------')

while True:
    numbera=input('Enter the first number\n')
    numbera=input('Enter the second number\n')

    operationType = input('Enter number from 1 to 4:\n1 - Adding\n2 - Subtracting\n3 - Multiplying\n4 - Dividing\n')
    if int(operationType)==1:
        result=numbera+numberb

print('---------------')
#crear una lista de 10 elementos que detecte el maximo
lista = [1,2,3,4,5,6,7,8,9,10]
print("Lista:", lista)
a = lista[0]  
for i in lista:
    if i > a:
        a = i

print("Numero maximo es:", a)




#[]  {}