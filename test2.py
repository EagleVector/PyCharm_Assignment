ascii_number = 65
rows = 7
i = 1
while i <= rows:
    j = 1
    while j <= i:
        character = chr(ascii_number)
        print(character, end=" ")
        ascii_number = ascii_number + 1
        j = j + 1

    print("\n")
    i = i + 1