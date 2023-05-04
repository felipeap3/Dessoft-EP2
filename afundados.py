def afundados(frota,tabuleiro):
    tamanho_navio = 0
    abates = []
    navio_abatidos = 0
    for navio,lista1 in  frota.items():
        for lista2 in lista1:
            abates=[]
            tamanho_navio = len(lista2)
            for coordenadas in lista2:
                x = coordenadas[0]
                y = coordenadas[1]
                if tabuleiro[x][y] == 'X':
                    abates.append('X')
            if len(abates) == tamanho_navio:
                navio_abatidos += 1
    return navio_abatidos

print(afundados({
    "porta-aviões":[
      [[1,5],[1,6],[1,7],[1,8]]
    ],
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
},[
  [0, '-', '-', 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 'X', 'X', 'X', 'X', 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, '-', '-', '-', '-', 0, 0],
  [0, '-', 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, '-', 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 'X', 0, 0, 0, 0, 1],
  [0, 1, 1, '-', '-', '-', '-', '-', '-', '-']
]))