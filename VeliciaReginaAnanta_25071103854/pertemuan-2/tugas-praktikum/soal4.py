# MENGHITUNG PANGKAT REKURSIF

a = int(input('Bilangan pokok: '))
b = int(input('Bilangan pangkat: '))

def pangkat_rekursif(a, b):
  hasil = a
  
  for x in range (b-1):
   hasil = hasil*a
  return hasil

hasil = (pangkat_rekursif(a, b))
print (f'hasil {a} pangkat {b} adalah {hasil}')
 
