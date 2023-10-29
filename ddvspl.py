def main():
    HP = float(input())
    ajmr = float(input())

    totalattack = int(input())

    adjustment = 0.0

    for _ in range(totalattack):
        damage = float(input())
        adjustment += 0.03 * damage
        HP - damage

    if HP <= 0:
        print("ดีดี้โดนัท")
    else:
        if adjustment >= ajmr:
            print("พาลอยซาชิมิ")
        else:
            print("ตายคู่")

main()
