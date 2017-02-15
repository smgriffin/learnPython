def find_nb(m):
    n = 0
    volume = 0
    while volume <= m:
        volume += (n + 1) ** 3
        n += 1
        print volume
    if volume > m:
        return -1
    else:
        return n


print(find_nb(500))
