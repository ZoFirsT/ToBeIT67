def main():
    total_num = 0

    while True:
        number = int(input())
        
        if number == -1:
            break
        
        total_num += number

    print(total_num)

main()
