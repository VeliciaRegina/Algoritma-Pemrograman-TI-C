class Vehicle:
   def __init__(self, jenis, merk, tahun_rilis):
      self.jenis = jenis
      self.merk = merk
      self.tahun_rilis = tahun_rilis

   def sound(self):
      return ("Suara")
   
class Car(Vehicle):
   def __init__(self, tahun_rilis):
      self.__tahun_rilis = tahun_rilis

   def get_tahun_rilis(self):
      return self.__tahun_rilis
   
   def set_tahun_rilis(self):
      return self.__tahun_rilis
   
   def sound(self):
      return ("Broommm")


class Motor(Vehicle):
   def __init__(self, tahun_rilis, merek):
      self.__tahun_rilis = tahun_rilis

   def get_tahun_rilis(self):
      return self.__tahun_rilis
   
   def set_tahun_rilis(self):
      return self.__tahun_rilis
   
   def sound(self):
      return ("Ngenggg")
   

v1 = Vehicle("Pesawat", 2016, "BoiengXXXXX")
c1 = Car(1999, "Ford")
m1 = Motor(2018, "Vario")

print(m1.sound())
print(c1.get_tahun_rilis())




   



