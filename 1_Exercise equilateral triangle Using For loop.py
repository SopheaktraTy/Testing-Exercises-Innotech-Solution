n = 5  

for i in range(1, n + 1):

    spaces = "" # this i do it by iterate the number of spaces before we append the stars. 
    for _ in range(n - i):
        spaces += " "

    stars = ""   
    for _ in range(2 * i - 1):
        stars += "*"

    print(spaces + stars)
