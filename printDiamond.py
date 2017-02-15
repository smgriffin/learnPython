def diamond(n):
    d = []
    if n % 2 == 0 or n <= 0:
        return 0
    else:
        for index in (list(range((n + 1) / 2)) + list(reversed(range(n / 2)))):
            d.append('{: <{w1}}{:*<{w2}}'.format('', '', w1=(n / 2) - index, w2=index * 2 + 1))
        return '\n'.join(d) + '\n'
