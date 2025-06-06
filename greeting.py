# return values

# def greet(input):
#     if "hello" in input:
#         return "hello, there"
#     else:
#         return "I'm not sure what you mean"

# greeting = greet("hi, computer")
# print(greeting)



#--------------------------------------- side effects usage of global 
emoticon = "v v"

def main():
    global emoticon
    say("Is anyone there?")

    emoticon = ":D"
    say("Oh!,  Hi...")

def say(phrase):
    print(phrase + " " + emoticon)
    
main()

#--------------------------------------- side effects usage of global 