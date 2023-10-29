def main(x, y, z):
    plusx = x + 10
    plusy = y + 10
    plusz = z + 10

    return plusx,plusy,plusz

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

plusx, plusy, plusz = main(x, y, z)

print(plusx, plusy, plusz)
