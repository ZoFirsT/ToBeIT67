def main():
    number_list = {
        0: 'rei',
        1: 'ichi',
        2: 'ni',
        3: 'san',
        4: 'shi',
        5: 'go',
        6: 'roku',
        7: 'shichi',
        8: 'hachi',
        9: 'kyu',
        10: 'ju',
        100: 'hyaku'
    }

    number = int(input().strip())

    print(number_list.get(number))

main()
