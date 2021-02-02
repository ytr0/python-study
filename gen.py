def product(xs, ys):
    for x in xs:
        for y in ys:
            yield x, y

def main():
    xs = [0, 1, 2]
    ys = ['a', 'b', 'c']

    for x, y in product(xs, ys):
        print(x, y)

main()