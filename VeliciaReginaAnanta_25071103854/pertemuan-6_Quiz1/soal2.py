buku = [["Algoritma", 2000], 
        ["Basis Data", 2500], 
        ["Satistika", 3000],
        ["Struktur Data", 2000],
        ["Pemrograman", 1500]
]

peminjaman = []

for x in range(len(buku)):
   print(f'{x+1}. {buku[x][0]} | Denda keterlambatan: {buku[x][1]}')
print('---------------------------------')

pilihan = int(input('Pilih buku: '))
while pilihan != 0:
   if 1 <= pilihan <= len(buku):
      lama = int(input('Lama peminjaman: '))
      judul = buku[pilihan-1][0]
      denda = buku[pilihan-1][1]
      peminjaman.append([judul, lama, denda])
   else:
      print('Opsi tidak valid')

   pilihan = int(input('Pilih buku: '))

print('\n=== DAFTAR BUKU DIPINJAM ===')
for x in range(len(peminjaman)):
   print(f'{x+1}. {peminjaman[x][0]} | lama: {peminjaman[x][1]}')

print('\n=== DENDA ===')
for x in range(len(peminjaman)):
   bayar = peminjaman[x][2] *1

   print(f'{x+1}. {peminjaman[x][0]} | denda: {bayar}')