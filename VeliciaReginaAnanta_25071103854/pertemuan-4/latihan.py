class Rekening:
   def __init__ (self, nama, saldo):
      self.nama = nama
      self.__saldo = saldo

   def cek_saldo(self):
      print(f'Saldo anda saat ini: {self.__saldo}')

   def setor(self):
      try:
         nominal = int(input('Nominal yang ingin di setor: '))

         if nominal < 0:
            print('Nominal harus lebih dari 0')
         else:
            self.__saldo += nominal
            self.cek_saldo()
         
      except ValueError:
         print('Nominal harus berupa bilangan bulat')
   
   def tarik(self):
      try:
         nominal = int(input('Nominal yang ingin di tarik: '))

         if nominal > self.__saldo:
            print('Saldo anda tidak cukup')
         elif nominal <= 0:
            print('Penarikan saldo harus lebih dari 0')
         else:
            self.__saldo -= nominal
            self.cek_saldo()

      except ValueError:
         print('Nominal harus berupa bilangan bulat')




p1 = Rekening("Velicia", 500_000)
print("""
---MENU TRANSAKSI---
1. cek saldo
2. setor
3. tarik
4. Keluar
--------------------""")
   
while True:   
   menu = int(input('Pilih Menu:'))

   match menu:
      case 1: p1.cek_saldo(), print ('\n')
      case 2: p1.setor(), print ('\n')
      case 3: p1.tarik(), print ('\n')
      case 4: break
      case _: print('Opsi tidak valid')