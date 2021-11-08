def Hello(func):
    def wrapper(*num):
        print("Hello!")
        a=func(*num)
        return a
    return wrapper

@Hello
def square(x):
    return x*x

print(square(15))