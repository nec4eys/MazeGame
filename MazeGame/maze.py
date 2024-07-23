import random

map_lab = []

path_true = []
path_false = []


def dead_end(b, a, key):
    global map_lab, path_false

    up_end = down_end = left_end = right_end = False

    if map_lab[b - 1][a] == 8:
        y_new_end = b - 1
        x_new_end = a
        if map_lab[y_new_end][x_new_end - 1] != 0 and \
                map_lab[y_new_end][x_new_end + 1] != 0 and \
                map_lab[y_new_end - 1][x_new_end] != 0:
            up_end = True

    if map_lab[b + 1][a] == 8:
        y_new_end = b + 1
        x_new_end = a
        if map_lab[y_new_end][x_new_end - 1] != 0 and \
                map_lab[y_new_end][x_new_end + 1] != 0 and \
                map_lab[y_new_end + 1][x_new_end] != 0:
            down_end = True

    if map_lab[b][a - 1] == 8:
        y_new_end = b
        x_new_end = a - 1
        if map_lab[y_new_end - 1][x_new_end] != 0 and \
                map_lab[y_new_end + 1][x_new_end] != 0 and \
                map_lab[y_new_end][x_new_end - 1] != 0:
            left_end = True

    if map_lab[b][a + 1] == 8:
        y_new_end = b
        x_new_end = a + 1
        if map_lab[y_new_end - 1][x_new_end] != 0 and \
                map_lab[y_new_end + 1][x_new_end] != 0 and \
                map_lab[y_new_end][x_new_end + 1] != 0:
            right_end = True

    if not up_end and not down_end and not left_end and not right_end:
        return None

    while True:
        rout = random.randrange(1, 5)

        if rout == 1 and up_end:
            y_new_end = b - 1
            x_new_end = a
            q_end = True
            break
        elif rout == 2 and down_end:
            y_new_end = b + 1
            x_new_end = a
            q_end = True
            break
        elif rout == 3 and left_end:
            y_new_end = b
            x_new_end = a - 1
            q_end = True
            break
        elif rout == 4 and right_end:
            y_new_end = b
            x_new_end = a + 1
            q_end = True
            break

    if q_end:
        st_end = [y_new_end, x_new_end]
        if key:
            path_false.append(st_end)
        map_lab[y_new_end][x_new_end] = 0
        dead_end(y_new_end, x_new_end, key)

    return None


def make_maze(d_lab, ch_lab):
    global map_lab, path_false, path_true

    d_lab += 2
    ch_lab += 2

    map_lab = [[8] * ch_lab for qi in range(d_lab)]  # заполняем массив восмерками (отсутствие знака)

    for i in range(d_lab):  # делаем рамку из еденичек
        for j in range(ch_lab):
            map_lab[0][j] = 1
            map_lab[d_lab - 1][j] = 1
            map_lab[i][0] = 1
            map_lab[i][ch_lab - 1] = 1

    xs = 1
    ys = d_lab - 2
    map_lab[ys][xs] = 2

    xf = ch_lab - 2
    yf = 1
    map_lab[yf][xf] = 3

    ch_lab -= 1
    d_lab -= 1

    path_s = [ys, xs]
    path_f = [yf, xf]
    path_true = []
    path_false = []

    path_true.append(path_s)

    while path_s != path_f:

        y = path_s[0]
        x = path_s[1]

        up = down = left = right = 0

        if 2 < x < ch_lab - 2 and 2 < y < d_lab - 2:
            up = 6
            down = 6
            right = 6
            left = 6

        if x == 2 or x == ch_lab - 2:
            if y == 2 or y == d_lab - 2:
                up = 12
                right = 12
                down = 0
                left = 0
            elif 2 < y < d_lab - 2:
                up = 8
                left = 8
                right = 8
                down = 0
        elif 2 < x < ch_lab - 2:
            if y == 2 or y == d_lab - 2:
                up = 8
                down = 8
                right = 8
                left = 0

        if (y != 1 and x == 1) or (x != ch_lab - 1 and y == d_lab - 1):
            up = 12
            right = 12
            down = 0
            left = 0

        if y == 1:
            if x == 1 or x == ch_lab - 2:
                right = 24
                up = 0
                down = 0
                left = 0
            else:
                right = 12
                down = 12
                up = 0
                left = 0

        if x == ch_lab - 1:
            if y == 2 or y == d_lab - 1:
                up = 24
                down = 0
                right = 0
                left = 0
            else:
                up = 12
                left = 12
                down = 0
                right = 0

        route = random.randrange(1, 25)

        side = ''
        y_new = x_new = 0

        if 0 < route <= up:
            x_new = x
            y_new = y - 1
            side = 'up'
        elif up < route <= up + down:
            x_new = x
            y_new = y + 1
            side = 'down'
        elif up + down < route <= up + down + left:
            y_new = y
            x_new = x - 1
            side = 'left'
        elif up + down + left < route <= up + down + left + right:
            y_new = y
            x_new = x + 1
            side = 'right'

        q = False
        if map_lab[y_new][x_new] == 8 or map_lab[y_new][x_new] == 3:
            if side == 'up':
                if map_lab[y_new][x_new - 1] != 0 and \
                        map_lab[y_new][x_new + 1] != 0 and \
                        map_lab[y_new - 1][x_new] != 0 and \
                        map_lab[y_new][x_new] != 0:
                    q = True
            elif side == 'down':
                if map_lab[y_new][x_new - 1] != 0 and \
                        map_lab[y_new][x_new + 1] != 0 and \
                        map_lab[y_new + 1][x_new] != 0 and \
                        map_lab[y_new][x_new] != 0:
                    q = True
            elif side == 'left':
                if map_lab[y_new - 1][x_new] != 0 and \
                        map_lab[y_new + 1][x_new] != 0 and \
                        map_lab[y_new][x_new - 1] != 0 and \
                        map_lab[y_new][x_new] != 0:
                    q = True
            elif side == 'right':
                if map_lab[y_new - 1][x_new] != 0 and \
                        map_lab[y_new + 1][x_new] != 0 and \
                        map_lab[y_new][x_new + 1] != 0 and \
                        map_lab[y_new][x_new] != 0:
                    q = True

        if q:
            st = [y_new, x_new]
            path_true.append(st)
            map_lab[y_new][x_new] = 0
            path_s = [y_new, x_new]

        else:
            p = o = m = c = 2
            if y_new + 2 > d_lab:
                p = 1
            if y_new - 2 < 0:
                o = 1
            if x_new + 2 > ch_lab:
                m = 1
            if x_new - 2 < 0:
                c = 1
            if (map_lab[y_new - o][x_new] == 0 or map_lab[y_new - 1][x_new - 1] == 0 or map_lab[y_new - 1][
                x_new + 1] == 0) and \
                    (map_lab[y_new + p][x_new] == 0 or map_lab[y_new + 1][x_new - 1] == 0 or map_lab[y_new + 1][
                        x_new + 1] == 0) and \
                    (map_lab[y_new][x_new + m] == 0 or map_lab[y_new - 1][x_new + 1] == 0 or map_lab[y_new + 1][
                        x_new + 1] == 0) and \
                    (map_lab[y_new][x_new - c] == 0 or map_lab[y_new - 1][x_new - 1] == 0 or map_lab[y_new + 1][
                        x_new - 1] == 0):
                x_r = path_f[1]
                y_r = path_f[0]
                y_min = y
                x_max = x
                r_min = ((x_r - x) ** 2 + (y_r - y) ** 2) ** 0.5
                for i in path_true:
                    if ((x_r - i[1]) ** 2 + (y_r - i[0]) ** 2) ** 0.5 <= r_min:
                        r_min = ((x_r - i[1]) ** 2 + (y_r - i[0]) ** 2) ** 0.5
                        y_min = i[0]
                        x_max = i[1]
                path_s = [y_min, x_max]

    if map_lab[1][ch_lab - 2] == 0:
        map_lab[2][ch_lab - 1] = 1
    elif map_lab[2][ch_lab - 1] == 0:
        map_lab[1][ch_lab - 2] = 1

    if map_lab[d_lab - 2][1] == 0:
        map_lab[d_lab - 1][2] = 1
    elif map_lab[d_lab - 1][2] == 0:
        map_lab[d_lab - 2][1] = 1

    t = 0
    for i in range(len(map_lab)):
        for j in range(len(map_lab[i])):
            if map_lab[i][j] == 8:
                t += 1

    if t > 1:
        n = 1
        while n != len(path_true) - 2:
            y = path_true[n][0]
            x = path_true[n][1]
            dead_end(y, x, True)
            n += 1

    n = 0
    while n != len(path_false):
        y = path_false[n][0]
        x = path_false[n][1]
        dead_end(y, x, False)
        n += 1

    for i in range(len(map_lab)):
        for j in range(len(map_lab[i])):
            if map_lab[i][j] == 8:
                map_lab[i][j] = 1

    return map_lab
