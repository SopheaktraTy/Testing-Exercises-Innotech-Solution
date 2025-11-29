n = 5  # height of the triangle

for i in range(1, n + 1):
    # build spaces
    spaces = ""
    for _ in range(n - i):
        spaces += " "

    # build stars
    stars = ""
    for _ in range(2 * i - 1):
        stars += "*"

    # print each line
    print(spaces + stars)
