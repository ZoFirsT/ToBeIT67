def main():
    letter_penetration = {
        'a': 2, 'f': 2, 'k': 2, 'p': 2, 'u': 2, 'z': 2,
        'b': 4, 'g': 4, 'l': 4, 'q': 4, 'v': 4,
        'c': 6, 'h': 6, 'm': 6, 'r': 6, 'w': 6,
        'd': 8, 'i': 8, 'n': 8, 's': 8, 'x': 8,
        'e': 10, 'j': 10, 'o': 10, 't': 10, 'y': 10
    }

    total_penetration = sum([letter_penetration[input().strip()] for _ in range(5)])

    if total_penetration >= 25:
        print("Unlock")
    else:
        print(25 - total_penetration)

main()
