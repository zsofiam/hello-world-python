
def get_hello_message():
    userinput = input("What's your name?")
    return "Hello " + userinput + "!"


def say_hello():
    print(get_hello_message())


say_hello()
