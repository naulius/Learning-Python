def create_cubes(n):
    result = []
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)

print(list(create_cubes(10)))

def gen_fibon(n):

    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b,a+b
    return output

for number in gen_fibon(10):
    print(number)


def simple_gen():
    for x in range(3):
        yield x

for x in simple_gen():
    print(number)

g = simple_gen()
print(next(g))