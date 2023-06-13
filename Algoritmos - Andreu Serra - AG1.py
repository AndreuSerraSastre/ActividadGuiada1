import numpy as np

def torres_hanoi(N, origen, destino, pivote):
  if N == 1:
    print(f"Mover bloque desde {origen} a {destino}")
    return
  
  torres_hanoi(N-1, origen, pivote, destino)
  print(f"Mover bloque desde {origen} a {destino}")
  torres_hanoi(N-1, pivote, destino, origen)

torres_hanoi(4, 1, 3, 2)

def cambio_monedas(cantidad, sistema):
  sistema.sort(reverse=True)
  print(f"Sistema: {sistema}")
  solucion = np.zeros(len(sistema), dtype=int)
  valor_acumulado = 0
  i = 0
  for moneda in sistema:
    monedas = int((cantidad - valor_acumulado)/moneda)
    solucion[i] = monedas
    valor_acumulado += monedas*moneda
    if valor_acumulado == cantidad:
      print(f"Solución: {solucion}")
      return solucion
    i += 1
  print("No es posible hacer cambio exacto con las monedas proporcionadas.")
  return None

def cambio_monedas(cantidad, sistema):
  sistema.sort(reverse=True)
  solucion = [0] * len(sistema)
  
  for i, moneda in enumerate(sistema):
    solucion[i], cantidad = divmod(cantidad, moneda)

  return solucion
