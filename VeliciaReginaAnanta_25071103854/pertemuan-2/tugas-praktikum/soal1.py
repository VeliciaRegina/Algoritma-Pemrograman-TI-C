# MENGHITUNG RATA-RATA DARI LIST NILAI

listNilai = [80, 75, 90, 60, 85]

def rata_rata(nilai):
   jumlah = 0
     
   if not nilai:
         return "Data kosong"
   else:
      for x in range(len(nilai)):
            jumlah += nilai[x]
         
   avg = jumlah / (len(nilai))
   return avg

      
print("Rata-rata: ", rata_rata(listNilai))