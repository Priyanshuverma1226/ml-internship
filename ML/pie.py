import math
print(math.pi)
# 3.141592653589793
# 2 -> 3.14
# 3 ->3.141
# 4 -> 3.1415

def next_pie(n):
    a=math.pi
    return round(a,n)

num=next_pie(int(input("ENter The Position :-")))
print(num)