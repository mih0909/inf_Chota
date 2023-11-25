def to(chislo, sys):
    """переводит из десятичной в sys-систему"""
    chislo = abs(chislo)
    a = '0123456789ABCDEF'
    s = ''
    while chislo != 0:
        digit = chislo % sys
        chislo = chislo // sys
        s = a[digit] + s
    return s


def frm(chislo, sys):
    """переврдит из sys-системы в десятичную"""
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
         '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    ln = len(chislo)
    n = 0
    p = 1
    while ln != 0:
        digit = chislo[ln - 1]
        if d.get(digit) > sys:
            return -1234567890
        n += d.get(digit) * p
        ln -= 1
        p *= sys
    return n
