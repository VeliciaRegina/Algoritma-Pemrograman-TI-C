n = int(input('Masukkan angka: '))

def jumlah_digit(n):
   if n <= 0:
      return 0
   else:
      digit = (n % 10) + jumlah_digit(n // 10)
      return digit
   
hasil = jumlah_digit(n)
print(f'Jumlah digit {n} adalah {hasil}')