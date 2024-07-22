#Print statement
print('Welcome to Python 101 on Scrimba')

#Variables
name = "Blessing"
print(name + ' ' + 'is learning the Python programming language.')

#Datatypes: Integer, Float, Boolean, String(camelcase, underscore),...whitespace count
a="it's"
b='it\'s'
print(a, b)

print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
#c1 = int("3.4")   # c1 will be...
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,d,e,f,g,h,i,j])

myButton = 'Ice cream'
price = 12.99
numberAvailable = 20

print(myButton, price, numberAvailable)

#Basic Arithmetic...multiplication, division, float, floor, modulus, exponent
a=10
b=3
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b) 

#Strings
name = 'blessing ogohhhhhhhh'
print(name*5)
print(name, name)
print(name + name)
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(len(name))
print(name.count('h')) #case sensitive
print(name[5])
print(name[-10]) #-1 is the last character
print(name[3:]) #grab everything including and after the first s
print(name[3:7]) #end point is specified
print(name[:5]) #grab everything including and before the first s


exercise = 'Welcome to Python 101: Strings'
exerciseName = 'Tyler'
solution = exercise[18] + ' ' + exercise[:8] + ' ' + exercise[25:29] + ' '  + exercise[8:10] + ' ' + exerciseName 
print(solution.title())
print(solution[::-1]) #print string backwards

# Multiple string lines
sample = """
Dear Blessing,
You are doing amazing. And,
all your dreams are valid.
"""
print(sample)


