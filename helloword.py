def hello_word():
    return "Hello,Word"


x = hello_word()
print(x)


def hello_word(name):
    if name == "" or name == None:
        return "Hello Word"
    else:
        return "Helllo"+ "! " + name


hello_word("Monika")
imie = input("Podaj imie:")
    

def print_hello(nameX):
    print(hello_word (nameX))


print_hello("Monika")







