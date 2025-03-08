import json

print("hello, world")

name = "mohak"
age = 21
pi = 3.148
is_dev = True

print(f"my name is {name}, {age} years old")

#lists 

tasks = ["build API", "lmao", "rofl"]
print(len(tasks))
tasks.append("kya re vedeya")
print(len(tasks))

# tuples = immutable lists

numbers = (10, 20)

# dict 

user = {"name": "mohak", "role": "dev"}

print(user["role"])

#loop 

for task in tasks :
    print(f"task: {task}")

for i in range(0,10) :
    print(i)    

count = 2 
while count > 0  : 
    print(count)
    count =-1 

def greet(name):
    return f"hello {name}"

print(greet("Mohak"))

try:
    result = 0/10
except ZeroDivisionError: 
    print("lil nigga learn division")
finally: 
    print("ye wala hmesha chalega bro chalega, kuch ho jaye")    


#oops 

class Person : 
    #this is like constructor
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def intro(self):
         print(f"kya re {name}, {age} ki umar mein bhi bakchodi") 

person1 = Person("Mohak", 21)  
person1.intro()  

with open("src/a.txt", "w") as f: 
    f.write("hello")

with open("src/a.txt", "r") as f: 
    content = f.read()

print(content)


json_data = json.dumps(user)
print(json_data)

parsed_data = json.loads(json_data)
print(parsed_data)