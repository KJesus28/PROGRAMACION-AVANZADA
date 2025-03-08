# -- coding: utf-8 --
"""
Created on Thu Vier  6 18:16:45 2025

@author: Ramirez Cruz
"""

n =int(input('Ingrese el numero que desea verificar'))
primo = True


for i in range(2,n-1):
    if (n % i) == 0:
        primo = False

print('El numero', n, 'Es primo?', primo)
