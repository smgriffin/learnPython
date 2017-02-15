def nb_year(p0, percent, aug, p):
    n = 0
    while p0 <= p:
        p0 += (p0 * percent * .01) + aug
        n += 1
    return n


n = nb_year(1500, 5, 100, 5000)
m = nb_year(1500000, 2.5, 10000, 2000000)
v = nb_year(1500000, 0.25, 1000, 2000000)
print n, m, v
