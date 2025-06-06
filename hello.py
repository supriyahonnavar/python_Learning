#input("What is your name? ")
#print("Hello, Supriya!")

# Ask the user for their name
# name = input("What is your name? ")
# print("Hello, ")
# print(name)


# Its another way of asking question
# name = input("What is your name? ")
# print("Hello,  " + name)

# Ask the user for their name
# name = input("What is your name? ")
# print('Hello, \"friend\"')
# # print(name)



# Ask the user for their name
# name = input("What is your name? ")
# print(f"Hello, {name}")

#-----------------

# # Ask the user for their name
# name = input("What is your name? ")

# # It removes the whitespace from str
# name = name.strip()

# #Capitalize user's name
# # name = name.capitalize()
# name = name.title()

# #Say hello to user
# print(f"Hello, {name}")


# # Ask the user for their name
# name = input("What's your name? ")

# # Remove whitespace from the str and capitalize the first letter of each word
# name = name.strip().title()

# # Print the output
# print(f"hello, {name}")



# # Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
# name = input("What's your name? ").strip().title()

# # Print the output
# print(f"hello, {name}")



# Demonstrates str functions

# name = input("What's your name? ").strip().title()
# first, last = name.split(" ")
# print(f"hello, {first}")


#------------------------------------------------------------------------
#defining function using def


# def hello():
#     print("Hello!!")

# name = input("Enter your name:")
# hello()
# print(name)
#------------------------------------------------------------------------
#defining function using def


# def hello(to):
#     print("Hello,", to)

# name = input("Enter your name:")
# hello(name)

# #------------------------------------------------------------------------
# #defining function using def


# def hello(to = "Honnavar"):
#     print("Hello,", to)

# hello()
# name = input("Enter your name:")
# hello(name)


# #------------------------------------------------------------------------
# # #defining function using def , main()
# def main():
#     name = input("Enter your name:")
#     hello(name)



# def hello(to = "world"):
#     print("Hello,", to)

# main()

#------------------------------------------------------------------------
# # #defining function using def , main()
def main():
    x = int(input("Enter a number:" ))
    print("x squared is:", square(x))


def square(n):
    #way 1
    return n * n

    #way 2
    # return pow(n, 2) 

    #way 3
    #return  n ** 2

main()


