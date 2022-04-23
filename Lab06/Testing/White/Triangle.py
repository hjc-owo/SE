def triangle(a, b, c):
    if a == int(a) and b == int(b) and c == int(c):
        if 1 <= a <= 10000 and 1 <= b <= 10000 and 1 <= c <= 10000 \
                and a + b > c and a + c > b and b + c > a:
            if a == b and b == c:
                return "equilateral triangle!"
            # elif a == b or b == c or a == c:
            #     return "isosceles triangle!"
            else:
                return "regular triangle!"
        else:
            return "not a triangle!"
    else:
        return "not a triangle!"
