def main():
    row = int(input())

    for i in range(1, row + 1):
        for j in range(i):
            print("#", end=" ")
        print()

main()
