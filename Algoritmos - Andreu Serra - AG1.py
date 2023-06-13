def torres_hanoi(N, origen, destino, pivote):
  if N == 1:
    print(f"Mover bloque desde {origen} a {destino}")
    return
  
  torres_hanoi(N-1, origen, pivote, destino)
  print(f"Mover bloque desde {origen} a {destino}")
  torres_hanoi(N-1, pivote, destino, origen)

torres_hanoi(4, 1, 3, 2)
