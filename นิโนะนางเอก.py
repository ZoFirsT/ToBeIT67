from decimal import Decimal
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = Decimal(input())
g = int(input())

ichika_per = a * g * f / Decimal(100)
nino_per = b * g * f / Decimal(100)
miku_per = c * g * f / Decimal(100)
yotsuba_per = d * g * f / Decimal(100)
itsuki_per = e * g * f / Decimal(100)

ichika_point = "Pass" if ichika_per > Decimal(60) else "Fail"
nino_point = "Pass" if nino_per > Decimal(60) else "Fail"
miku_point = "Pass" if miku_per > Decimal(60) else "Fail"
yotsuba_point = "Pass" if yotsuba_per >= Decimal(60) else "Fail"
itsuki_point = "Pass" if itsuki_per > Decimal(60) else "Fail"

pass_point = sum([ichika_point == "Pass", nino_point == "Pass", miku_point == "Pass", yotsuba_point == "Pass", itsuki_point == "Pass"])

print(f"Ichika : {ichika_point}")
print(f"Nino : {nino_point}")
print(f"Miku : {miku_point}")
print(f"Yotsuba : {yotsuba_point}")
print(f"Itsuki : {itsuki_point}")

if pass_point < 3:
    print("Futaro Outtt!!!")