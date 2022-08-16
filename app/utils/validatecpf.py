import random


def validateGenCpf():
    sum, leftover = 0, 0
    multiplier1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    multiplier2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    seed = str(random.randint(100000000, 999999999))

    for i in range(9):
        sum += int(seed[i]) * multiplier1[i]

    leftover = sum % 11
    if leftover < 2:
        leftover = 0
    else:
        leftover = 11 - leftover

    seed = seed + str(leftover)
    sum = 0

    for i in range(10):
        sum += int(seed[i]) * multiplier2[i]

    leftover = sum % 11

    if leftover < 2:
        leftover = 0
    else:
        leftover = 11 - leftover

    seed = seed + str(leftover)
    formated = f"{seed[0:3]}.{seed[3:6]}.{seed[6:9]}-{seed[9:11]}"
    return (seed, formated)
