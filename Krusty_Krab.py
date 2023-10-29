def main():
    book_codes = []
    while True:
        code = input().strip()
        if code.lower() == "end":
            break
        book_codes.append(code)

    sorted_codes = sorted(book_codes)

    book_data = []
    for code in sorted_codes:
        if any(item[0] == code for item in book_data):
            continue

        first_occurrence = book_codes.index(code) + 1  # 1-based index
        total_occurrences = book_codes.count(code)

        book_data.append((code, first_occurrence, total_occurrences))

    for item in book_data:
        print(f"{item[0]} {item[1]} {item[2]}")

main()
