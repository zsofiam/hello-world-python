def get_user_name():
    userinput = input("What's your name?")
    return userinput.capitalize()


def get_hello_message(name):
    if name == "":
        name = "World"
    return "Hello, " + name + "!"


def say_hello():
    print(get_hello_message(get_user_name()))


say_hello()
