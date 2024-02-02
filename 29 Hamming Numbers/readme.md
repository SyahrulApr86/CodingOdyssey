## Pendekatan Naif dalam Menghasilkan Hamming Number

### Pendahuluan

Hamming Numbers adalah serangkaian bilangan yang hanya memiliki faktor prima 2, 3, dan 5. Urutan Hamming Numbers dimulai dari 1 (dianggap sebagai Hamming Number karena $2^0 \times 3^0 \times 5^0 = 1$ ), diikuti oleh 2, 3, 4, 5, 6, 8, 9, 10, 12, dan seterusnya. Konsep ini dinamai menurut Richard Hamming, seorang ilmuwan komputer. 

Kode yang disediakan di bawah ini menunjukkan pendekatan naif untuk menemukan Hamming Number ke-N. Pendekatan naif berarti kode tersebut menggunakan metode yang paling langsung dan sederhana, meskipun mungkin tidak efisien untuk kasus dengan nilai N yang besar.

### Kode

```python
def is_hamming_number(n):
    if n == 1:
        return True
    if n <= 0:
        return False
    for prime in [2, 3, 5]:
        while n % prime == 0:
            n /= prime
    return n == 1

def hamming_naive(N): # --> not optimal and will cause time limit exceeded
    count, number = 0, 1
    while True:
        if is_hamming_number(number):
            count += 1
            if count == N:
                return number
        number += 1
```
Kode ini terdiri dari dua fungsi utama:

#### 1. `is_hamming_number(n)`

Fungsi ini memeriksa apakah suatu bilangan `n` adalah Hamming Number. Ia melakukan ini dengan terus membagi `n` dengan 2, 3, dan 5 (faktor prima dari Hamming Numbers) hingga `n` tidak lagi habis dibagi oleh angka-angka tersebut. Jika hasil akhirnya adalah 1, maka `n` adalah Hamming Number.

#### 2. `hamming_naive(N)`

Fungsi ini mencari Hamming Number ke-N menggunakan pendekatan naif. Ia melakukannya dengan menghitung mulai dari 1 dan memeriksa setiap bilangan secara berurutan apakah itu Hamming Number dengan menggunakan fungsi `is_hamming_number`. Ketika jumlah Hamming Number yang ditemukan mencapai N, fungsi tersebut mengembalikan Hamming Number tersebut.

### Kompleksitas

#### Waktu

Pendekatan naif ini memiliki kompleksitas waktu yang tinggi, terutama karena setiap bilangan perlu diperiksa satu per satu hingga menemukan Hamming Number ke-N. Kompleksitas waktu akan menjadi O(NlogN) dalam kasus terburuk, karena untuk setiap bilangan, kita mungkin perlu melakukan beberapa pembagian hingga menentukan apakah itu Hamming Number.

#### Ruang

Kompleksitas ruang dari kode ini relatif rendah karena hanya memerlukan penyimpanan untuk sejumlah variabel sederhana dan tidak mengalokasikan memori tambahan yang signifikan selama eksekusi.

### Kelebihan dan Kekurangan

#### Kelebihan

- **Sederhana dan Mudah Dipahami**: Pendekatan naif mudah untuk dipahami dan diimplementasikan, membuatnya menjadi titik awal yang baik untuk belajar tentang Hamming Numbers.

#### Kekurangan

- **Tidak Efisien untuk Nilai N yang Besar**: Karena setiap bilangan diperiksa satu per satu, waktu eksekusi menjadi sangat lambat untuk nilai N yang besar.
- **Batas Waktu Terlampaui**: Dalam praktiknya, pendekatan ini mungkin tidak praktis untuk aplikasi nyata atau kasus pengujian dengan nilai N yang sangat besar karena akan menyebabkan batas waktu eksekusi terlampaui (time limit exceeded).


