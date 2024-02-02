# Pendahuluan

Hamming Numbers adalah serangkaian bilangan yang hanya memiliki faktor prima 2, 3, dan 5. Urutan Hamming Numbers dimulai dari 1 (dianggap sebagai Hamming Number karena $2^0 \times 3^0 \times 5^0 = 1$ ), diikuti oleh 2, 3, 4, 5, 6, 8, 9, 10, 12, dan seterusnya. Konsep ini dinamai menurut Richard Hamming, seorang ilmuwan komputer. 

## Pendekatan Naif dalam Menghasilkan Hamming Number
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
---
## Pendekatan Menggunakan Heap untuk Menghasilkan Hamming Number

Dalam pencarian Hamming Number ke-N, pendekatan yang lebih canggih dan efisien daripada metode naif adalah menggunakan struktur data heap. Heap memungkinkan kita untuk menjaga elemen dalam urutan terurut tanpa perlu melakukan sortir manual pada setiap iterasi, yang sangat meningkatkan efisiensi waktu terutama untuk nilai N yang besar.

### Kode

Kode ini menggunakan modul `heapq` dari Python untuk mengimplementasikan heap, yang merupakan priority queue. Algoritma ini menghasilkan Hamming Number ke-N dengan cara yang efisien.

#### Fungsi `hamming_deque(N)`

Fungsi ini mencari Hamming Number ke-N menggunakan struktur data heap. Ia bekerja dengan cara berikut:

- **Inisialisasi**: Heap diinisialisasi dengan angka 1, yang juga merupakan Hamming Number pertama. Sebuah set `seen` digunakan untuk menghindari duplikasi nilai dalam heap.
- **Iterasi**: Untuk setiap iterasi hingga N, elemen terkecil diambil dari heap (yang dijamin menjadi Hamming Number berikutnya) dan kemudian dihilangkan dari heap.
- **Penggandaan dan Penyaringan**: Untuk setiap elemen yang diambil, kita mengalikan dengan setiap faktor (2, 3, dan 5) untuk mendapatkan kandidat Hamming Number berikutnya. Jika kandidat belum ada di dalam set `seen`, maka ditambahkan ke heap dan set `seen`.
- **Pengembalian Nilai**: Proses ini berlanjut hingga kita mencapai iterasi ke-N, di mana fungsi mengembalikan nilai terakhir yang diambil dari heap sebagai Hamming Number ke-N.

### Kompleksitas

#### Waktu

Pendekatan ini memiliki kompleksitas waktu yang jauh lebih baik daripada pendekatan naif, terutama karena operasi heap (penambahan dan penghapusan) yang efisien. Operasi heap berjalan dalam waktu O(log n) untuk setiap penambahan atau penghapusan, membuat keseluruhan algoritma berjalan dalam waktu O(N log N), dimana N adalah jumlah Hamming Number yang ingin dihasilkan.

#### Ruang

Kompleksitas ruang dari pendekatan ini juga efisien. Heap dan set `seen` bersama-sama menyimpan tidak lebih dari 3N elemen pada waktu tertentu (dalam praktiknya, jumlahnya akan jauh lebih kecil karena banyak nilai yang tidak unik dan tidak ditambahkan ke heap). Ini membuat kompleksitas ruang menjadi O(N).

### Kelebihan dan Kekurangan

#### Kelebihan

- **Efisien untuk Nilai N yang Besar**: Dengan menggunakan heap, kita dapat secara efisien menghasilkan Hamming Number ke-N bahkan untuk nilai N yang sangat besar.
- **Pengurutan Otomatis**: Heap menjaga elemen dalam urutan terurut, sehingga tidak perlu sortir manual yang memakan waktu.

#### Kekurangan

- **Kompleksitas Implementasi**: Walaupun kode ini lebih pendek daripada pendekatan naif, pemahaman tentang cara kerja heap diperlukan untuk memahami sepenuhnya algoritma ini.

### Kesimpulan

Pendekatan menggunakan heap untuk menghasilkan Hamming Number ke-N adalah metode yang sangat efisien dan efektif, khususnya untuk nilai N yang besar. Dengan memanfaatkan operasi heap yang cepat, algoritma ini mengurangi waktu eksekusi yang diperlukan dibandingkan dengan pendekatan naif. Pendekatan ini ideal untuk aplikasi yang memerlukan pencarian Hamming Number dalam urutan yang besar dengan waktu eksekusi yang minimal.

