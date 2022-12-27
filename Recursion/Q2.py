fir = int(input())
sec = input()
sec = sec.split()
sec = [int(i) for i in sec]
descarte = False

def jogada(sec,descarte,jg_salvas={},soma=0):
    chave = (tuple(sec),descarte,soma)
    if chave in jg_salvas:
        return jg_salvas[chave]
        
    if len(sec) == 0:
        return soma

    if descarte:
        jg_esq = jogada(sec[1:],not descarte,jg_salvas, soma+0)
        jg_dir = jogada(sec[:-1],not descarte,jg_salvas, soma+0)
    else:
        jg_esq = jogada(sec[1:],not descarte,jg_salvas,soma+sec[0])
        jg_dir = jogada(sec[:-1],not descarte,jg_salvas, soma+sec[-1])
    
    jg_salvas[chave] = max(jg_esq,jg_dir)
    
    return max(jg_esq,jg_dir)

if len(sec) == fir and (1 < fir and fir < 101):
    print(jogada(sec,descarte))