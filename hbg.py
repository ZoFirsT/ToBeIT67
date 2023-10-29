def main():
    '''Main Function'''

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    time_buy = d // (b + c)

    hbg = time_buy * (b + c)

    rem__hbg = d - hbg

    cost = time_buy * b * a

    if rem__hbg > 0:
        if rem__hbg > b:
            cost += b * a
            hbg += (b + c)
        else:
            cost += rem__hbg * a
            hbg += rem__hbg

    print(hbg, "ชิ้น")
    print(cost, "บาท")


main()
