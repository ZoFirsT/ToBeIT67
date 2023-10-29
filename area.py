import math

def clu_area(r, p):
    bomb_area = math.pi * (r**2)
    
    if p >= 2 * bomb_area:
        return "Not Safe"
    else:
        return "Safe"

r = int(input())
p = int(input())
    
answer = clu_area(r, p)
print(answer)
