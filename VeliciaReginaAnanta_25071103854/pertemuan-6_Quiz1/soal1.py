buku = [["Algoritma", 2000], 
        ["Basis Data", 2500], 
        ["Satistika", 3000],
        ["Struktur Data", 2000],
        ["Pemrograman", 1500]
]

for x in range(len(buku)):
   print(f'{x+1}. {buku[x][0]} | Denda keterlambatan: {buku[x][1]}')

pilihan = int(input('\nMasukkan buku yang dipilih (nomor): '))

if 1 <= pilihan <= len(buku):
   print(f'\nJudul buku: {buku[pilihan-1][0]} | Denda: {buku[pilihan-1][1]}')
else:
   print('Pilihan tidak valid')