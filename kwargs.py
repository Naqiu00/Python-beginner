# **kwargs = parameter that pack arguments into dictionary. useful so that function can accept varying keyword arguments

def hello(**kwargs):
    # print("Hello "  + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title = "Dr.", first = "Chris", middle = "Jack", last = "Patt")