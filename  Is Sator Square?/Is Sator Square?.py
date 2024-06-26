def is_sator_square(tablet):
    A = {''.join(a) for a in tablet}
    B = {''.join(a)[::-1] for a in tablet}
    C = {''.join(a) for a in zip(*tablet)}
    D = {''.join(a)[::-1] for a in zip(*tablet)}
    return A == B == C == D

tablet1 = [
    ['B', 'A', 'T', 'S'],
    ['A', 'B', 'U', 'T'],
    ['T', 'U', 'B', 'A'],
    ['S', 'T', 'A', 'B']
]
tablet2 = [
    ['R', 'O', 'T', 'O'],
    ['O', 'D', 'E', 'R'],
    ['T', 'E', 'N', 'O'],
    ['O', 'R', 'O', 'T']
]
print(is_sator_square(tablet1))
print(is_sator_square(tablet2))
