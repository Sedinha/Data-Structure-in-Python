s = input("")


def caçapalindromo(s):
    abc = list("abcdefghijklmnopqrstuvwxyz")
    sl = list(s)
    i = 0
    while i < len(sl):
        for letra in abc:
            if sl[i] != letra:
                salvo = sl[i]
                sl[i] = letra
                if sl == sl[::-1]:
                    return print("POSSÍVEL")
                else:
                    sl[i] = salvo
        i += 1
    return print("IMPOSSÍVEL")


caçapalindromo(s)
