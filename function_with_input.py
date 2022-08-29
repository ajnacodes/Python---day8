# def greet():
#     print("Welcome to day 8!")
#     print("Today we'll learn functions with inputs")
#     print("And by the end of the day we'll learn to encode and decode!")

# greet()   


# functions with inputs
#  def my_function(something):
#    do this with something 
#    then do this 
#    then finally do this 

#  my_function(123)

# something (Parameter) = 123 (Argument)
# the Parameter is the name of the data that's being passed in
# the Argument is the actual value of the data

# function that allows for input

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do, {name}?")
    
greet_with_name("Daniela")