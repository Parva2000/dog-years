def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"
print(dog_years("flora", 5))

def lots_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second 
    fourth = third % a

    print(first)
    print(second)
    print(third)

    return fourth
print(lots_of_math(5, 10, 15, 20))