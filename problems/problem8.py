import math

def encryption(input):
    input = input.replace(" ", "")
    size = len(input)
    lowerbound = int(math.floor(math.sqrt(size)))
    upperbound = int(math.ceil(math.sqrt(size)))
    total = upperbound * lowerbound

    while total < size:
        if lowerbound < upperbound:
            lowerbound += 1
        else:
            upperbound += 1
        total = upperbound * lowerbound

    grid = [["" for _ in range(upperbound)] for _ in range(lowerbound)]
    index = 0

    for row in range(lowerbound):
        for col in range(upperbound):
            if index < len(input):
                grid[row][col] = input[index]
                index += 1

    encrypted = ""

    for col in range(upperbound):
        for row in range(lowerbound):
            if grid[row][col] != "":
                encrypted += grid[row][col]

        if col != upperbound - 1:
            encrypted += " "

    return encrypted

text = "if man was meant to stay on the ground god would have given us roots"
encrypted_text = encryption(text)
print(encrypted_text)