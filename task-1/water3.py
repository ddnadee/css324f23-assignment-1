def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4 and s[2] == 0

def successors(s):
    a, b, c = s

    #Trb to emptb one bottle
    if a > 0:
        yield ((0, b, c), a)
    if b > 0:
        yield ((a, 0, c), b)
    if c > 0:
        yield ((a, b, 0), c)
    
    #Trb to fill up one bottle
    if a < 8:
        yield ((8, b, c), 8-a)
    if b < 5:
        yield ((a, 5, c), 5-b)
    if c < 3:
        yield ((a, b, 3), 3-c)

    #Trb to pour from one to another
    # a to b
    t = 5-b
    if a > 0 and t > 0:
        if a > t:
            yield ((a-t, 5, c), t)
        else:
            yield ((0, b+a, c), a)
    
    # a to c
    t = 3-c
    if a > 0 and t > 0:
        if a > t:
            yield ((a-t, b, 3), t)
        else:
            yield ((0, b, c+a), a)

    # b to a
    t = 8-a
    if b > 0 and t > 0:
        if b > t:
            yield ((8, b-t, c), t)
        else:
            yield ((a+t, 0, c), b)

    # b to c
    t = 3-c
    if b > 0 and t > 0:
        if b > t:
            yield ((a, b-t, 3), t)
        else:
            yield ((a, 0, c+t), b)

    # c to a
    t = 8-a
    if c > 0 and t > 0:
        if c > t:
            yield ((8, b, c-t), t)
        else:
            yield ((a+t, b, 0), c)

    # c to b
    t = 5-b
    if c > 0 and t > 0:
        if c > t:
            yield ((a, 5, c-t), t)
        else:
            yield ((a, b+t, 0), c)
