def print_staircase(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        hashes = '#' * i
        print(spaces + hashes)

# Example usage:
n = 4
print_staircase(n)
