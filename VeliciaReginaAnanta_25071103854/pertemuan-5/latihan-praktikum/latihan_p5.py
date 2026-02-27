A = [
   [5, 3, 1], 
   [2, 8, 4], 
   [6, 0, 7]] 

B = [
   [1, 2, 3], 
   [4, 5, 6], 
   [7, 8, 9]]

#TAMBAH
def tambah_matriks(A, B): 
    if len(A) != len(B) or len(A[0]) != len(B[0]): 
        print('Error: ukuran matriks tidak sama') 
        return None 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] + B[i][j] for j in range(kolom)] for i in range(baris)] 
    return hasil
C_tambah = tambah_matriks(A, B)
print('Tambah Matriks')
for baris in C_tambah:
    print(baris)

      
#KURANG
def kurang_matriks(A, B): 
    if len(A) != len(B) or len(A[0]) != len(B[0]): 
        print('Error: ukuran matriks tidak sama') 
        return None 
    baris, kolom = len(A), len(A[0]) 
    hasil = [[A[i][j] - B[i][j] for j in range(kolom)] for i in range(baris)] 
    return hasil 
C_kurang = kurang_matriks(A, B)
print('\nKurang Matriks')
for baris in C_kurang:
    print(baris)


#SKALAR
def kali_skalar(matriks, k): 
   hasil = [] 
   for baris in matriks: 
      baris_baru = [elemen * k for elemen in baris] 
      hasil.append(baris_baru) 
   return hasil 
C_skalar = kali_skalar(A, 4)
print('\nKali Matriks')
for baris in C_skalar:
    print(baris)

#DETERMINAN
def determinan_3x3(M): 
    # Diagonal utama: dijumlahkan 
    d1 = M[0][0] * M[1][1] * M[2][2] 
    d2 = M[0][1] * M[1][2] * M[2][0] 
    d3 = M[0][2] * M[1][0] * M[2][1] 
    # Diagonal sekunder: dikurangkan 
    d4 = M[0][2] * M[1][1] * M[2][0] 
    d5 = M[0][0] * M[1][2] * M[2][1] 
    d6 = M[0][1] * M[1][0] * M[2][2] 
    return (d1 + d2 + d3) - (d4 + d5 + d6)

print('\nDeterminan')
print('det(A):', determinan_3x3(A))
print('det(B):', determinan_3x3(B))