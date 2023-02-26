from math import pi, tan
s = int(input())
l = int(input())
area = round(s * (l**2)/(4*tan(pi/s)))
print(area)