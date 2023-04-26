def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicoes = []
    i = 0
    for i in range(tamanho):
        if orientacao == 'vertical':
            lista_posicoes.append([linha+i,coluna])
        elif orientacao == 'horizontal':
            lista_posicoes.append([linha,coluna+i])
    return lista_posicoes



print(define_posicoes(2,4,'vertical',3))