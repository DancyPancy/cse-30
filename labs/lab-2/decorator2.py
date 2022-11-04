def decorator(func):       
    def wrap():
        print("======")
        func()
        print("======")
    return wrap

@decorator
def printName():
    print("John!")

if __name__ == '__main__':
    printName()

print()
# create a decorator that takes in parameters
def run_times (num):
    def wrap (func):
        for i in range (num):
            func( )
    return wrap

@run_times(4)
def sayHello( ):
    print("Hello!", end=" ")

print()
# create a decorator for a function that accepts parameters
def birthday(func):
    def wrap(name, age):
        func(name, age + 1)
    return wrap

@birthday
def celebrate(name, age):
    print( "Happy birthday {}, you are now {}.".format(name, age) )

celebrate("Paul", 43)

# restrict function access
def login_required(func):
    def wrap(user):
        password = input("What is the password?")
        if password == user["password"]:
            func(user)
        else: 
            print("Access Denied")
    return wrap

@login_required
def restrictedFunc(user):
    print( "Access granted, welcome {}!".format(user["name"]))

user = { "name" : "Jess", "password" : "ilywpf" }
restrictedFunc(user)