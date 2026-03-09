minggu = int(input('Minggu: '))
buku = int(input('Buku: '))

matriks = []

for x in range(minggu):
   baris = [] 
   
   print(f'\nMinggu ke-{x+1}: ')
   for y in range(buku):
      book = int(input((f'Buku ke-{y+1}: ')))
      baris.append(book)
   
   matriks.append(baris)

print('\n=== Matriks Penjualan ===')
for x in range (minggu):
   for y in range(buku):
      print(matriks[x][y], end=' ')
   print('')


print('\n=== Total Penjulan dalam Minggu ===')
for x in range(minggu):
   totalMinggu = sum(matriks[x])
   print(f'Total Minggu ke-{x+1}: {totalMinggu}')

print('\n=== Total Penjulan dalam Buku ===')
for x in range(minggu):
   totalBuku = 0
   for y in range(buku):
      totalBuku += matriks[y][x]
   print(f'Total Buku ke-{x+1}: {totalBuku}')






