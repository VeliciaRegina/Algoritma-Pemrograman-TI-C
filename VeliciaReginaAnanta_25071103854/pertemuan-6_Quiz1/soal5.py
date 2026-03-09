class Buku:
   def __init__(self, judul, denda_per_hari):
      self.judul = judul
      self.denda_per_hari = denda_per_hari

   def tampilkan(self):
      print(f'{self.judul} - Denda: Rp{self.denda_per_hari}')

class Peminjaman(Buku):
   def __init__(self):
      self.total_denda = 0

   def tambah(self, buku, hari_keterlambatan):
      self.hari_keterlambatan = hari_keterlambatan 

   def ringkasan(self):
      print(f'Hari keterlambatan: {self.hari_keterlambatan}')

p1 = Buku('Algoritma', 2000)
p2 = Buku('Basis Data', 2500)
p3 = Buku('Satistika', 3000)

bukuPinjam = [p1, p2, p3]

for x in range(len(bukuPinjam)):
   print(f'{x+1}. ', end ='')
   bukuPinjam[x].tampilkan()
print('------------------------------------')

peminjaman1 = Peminjaman()
pilihaan = int(input('Pilihan(nomor): '))
keterlambatan = int(input('Hari keterlambatan: '))
bukuDipilih = bukuPinjam[pilihaan-1]

peminjaman1.tambah(bukuDipilih, keterlambatan)
peminjaman1.ringkasan()

