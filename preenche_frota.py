def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicoes = []
    i = 0
    for i in range(tamanho):
        if orientacao == 'vertical':
            lista_posicoes.append([linha+i,coluna])
        elif orientacao == 'horizontal':
            lista_posicoes.append([linha,coluna+i])
    return lista_posicoes

def preenche_frota(frota,navio,linha,coluna,orientacao,tamanho):
    if navio not in frota:
        frota[navio] = [define_posicoes(linha,coluna,orientacao,tamanho)]
    elif navio in frota:
        frota[navio].append(define_posicoes(linha,coluna,orientacao,tamanho)) 
    return frota
   



print(preenche_frota({"navio-tanque":[[[6,1],[6,2],[6,3]]]},'navio-tanque',4,7,'vertical',3))