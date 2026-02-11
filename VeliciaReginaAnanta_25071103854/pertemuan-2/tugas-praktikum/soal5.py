# MENGHITUNG JARAK DUA TITIK PADA BIDANG KARTESIUS
import math

x1 = int(input('Input x1 : '))
y1 = int(input('Input y1 : '))
x2 = int(input('Input x2 : '))
y2 = int(input('Input y2 : '))

def jarak(x1, y1, x2,y2):
   sumbuX = x2 - x1
   sumbuY = y2 - y1
   kuadrat = (sumbuX ** 2) + (sumbuY ** 2)
   sqrt = math.sqrt(kuadrat)
   return sqrt

hasil = jarak(x1, y1, x2,y2)
print (f'Jarak = {hasil}')