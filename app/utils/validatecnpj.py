# from > https://gist.github.com/lucascnr/24c70409908a31ad253f97f9dd4c6b7c < /
import random


def generate_cnpj():
    cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]

    for _ in range(2):
        value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
        digit = 11 - value % 11
        cnpj.append(digit if digit < 10 else 0)

    seed = "".join(str(x) for x in cnpj)
    formated = f"{seed[0:2]}.{seed[2:5]}.{seed[5:8]}/{seed[8:12]}-{seed[12:14]}"
    return (seed, formated)


generate_cnpj()
