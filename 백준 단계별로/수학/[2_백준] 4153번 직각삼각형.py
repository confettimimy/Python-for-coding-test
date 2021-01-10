def is_right_angle_triangle(side1, side2, side3):
    tmp_ls = [side1, side2, side3]
    tmp_ls.sort()

    if (tmp_ls[-1])**2 == (tmp_ls[0])**2 + (tmp_ls[1])**2:
        print("right")
    else:
        print("wrong")


while True:
    a, b, c = map(int, input().split())

    if a==0 and b==0 and c==0:
        break

    is_right_angle_triangle(a, b, c)
