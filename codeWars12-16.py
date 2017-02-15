from sys import argv


def tickets(people):
    bank = 0
    line = people
    if line[0] == 25:
        for people in line:
            bank += line[people] - 25
            if bank / line[people] < 1:
                return 'No'
        return 'Yes'
    else:
        return 'No'


lineup = []
lineup = argv
