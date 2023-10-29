def main():
    soupprices = {
        "shrimp sour soup": 80,
        "mixed vegetables sour soup": 60,
        "papaya sour soup": 55,
        "snapper fish sour soup": 100,
        "cha om shrimp sour soup": 100,
    }

    totalprice = 0
    soupcount = 0

    while True:
        soup = input()
        if soup == "stop":
            break
        
        if soup in soupprices:
            totalprice += soupprices[soup]
            soupcount += 1

    discount = 0
    if totalprice >= 200 and soupcount >= 3:
        discount = totalprice * 0.15

    final = totalprice - discount

    print(f"original price {totalprice} baht")
    print(f"discount {int(discount)} baht")
    print(f"total {int(final)} baht")
main()