heads = 35
legs = 94
def solve(numheads, numlegs):
    r = None
    c = None
    # nh = numheads
    # nl = numlegs
    # r + c = nh => r = nh - c
    # 4*r + 2*c = nl => 4*nh - 2*c = nl => c = 2*nh - nl/2 
    c = 2*numheads - numlegs/2
    r = numheads - (2*numheads - numlegs/2)
    print(int(r), "rabbits,", int(c), "chickens")
solve(heads, legs)
