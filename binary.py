def main():
    numbers = []

    while True:
        n = input()
        if n == "END":
            break
        n = int(n)
        numbers.append(n)

    processed = []

    for num in numbers:
        if num not in processed:
            count = numbers.count(num)
            total = num + count
            print(f"{num}-->{bin(total)[2:]}")
            processed.append(num)

if __name__ == "__main__":
    main()
