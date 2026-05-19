data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]

def radix_sort(arr):
   data = arr.copy()
   radixArray = [[], [], [], [], [], [], [], [], [], []]
   maxVal = max(data)
   exp = 1

   while maxVal // exp > 0:
      while len(data) > 0:
         val = data.pop()
         radixIndex = (val // exp) % 10
         radixArray[radixIndex].append(val)

      for bucket in radixArray:
         while len(bucket) > 0:
            val = bucket.pop()
            data.append(val)

      exp *= 10
   
   return data

def mergeSort(arr):
   if len(arr) <= 1:
      return arr

   mid = len(arr) // 2
   leftHalf = arr[:mid]
   rightHalf = arr[mid:]

   sortedLeft = mergeSort(leftHalf)
   sortedRight = mergeSort(rightHalf)
   return merge(sortedLeft, sortedRight)

def merge(left, right):
   result = []
   i = j = 0

   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         result.append(left[i])
         i += 1
      else:
         result.append(right[j])
         j += 1

   result.extend(left[i:])
   result.extend(right[j:])
   return result

def linear_search(arr, num):
   data = radix_sort(arr)
   for i in range(len(data)):
      if data[i] == num:
         return i
   return -1

def binary_search(arr, num):
   data = mergeSort(arr)

   left = 0
   right = len(data) - 1

   while left <= right:
      mid = (left + right) // 2

      if data[mid] == num:
         return mid
      elif data[mid] < num:
         left = mid + 1
      else:
         right = mid - 1
   return -1

print('Sebelum sort: ', data)
print('\nSetelah radix sort:', radix_sort(data))
print('\n\nSebelum sort: ', data)
print('\nSetelah merge sort:', mergeSort(data))

print()
print('-'*50)
first_num = int(input('Masukkan angka pertama yang ingin dicari: '))
second_num = int(input('Masukkan angka kedua yang ingin dicari: '))

cari1 = linear_search(data, first_num)
cari2 = binary_search(data, second_num)
cari = [[first_num, second_num], [cari1, cari2]]

for x in range(len(cari)):
   if cari[1][x] == -1:
      print(f'{cari[0][x]} tidak ada.')
      continue
   else:
      print(f'{cari[0][x]} ditemukan di indeks {cari[1][x]}')