def divisible(fun):
    def new_divisble(x):
        if x % 5 == 0:
            print(f"{x} is divisble by 5")
            fun(x)
            print ("I am just checking out")
        else:
            print(f"{x} it is not divisible by 5")
    return new_divisble

@divisible
def divide(x):
    print("I am a number:{x}")


divide(10)
