
database = {}


def expensive_seq(x, y, z):
    if (x, y, z) in database:
        return database[(x, y, z)]
    else:

        if x <= 0:
            database[(x, y, z)] = y + z
            return database[(x, y, z)]
        if x > 0:
            answer = expensive_seq(
                x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
            database[(x, y, z)] = answer
            return database[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
