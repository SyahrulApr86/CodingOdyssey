

# Perbandingan Algoritma: Penyelesaian "Multiples of 3 and 5"

Dokumen ini membahas perbandingan antara dua algoritma yang berbeda untuk menyelesaikan masalah yang sama, yaitu menemukan jumlah semua bilangan di bawah `number` yang habis dibagi 3 atau 5. Kita akan membandingkan dua algoritma tersebut dari sisi kompleksitas algoritma serta memberikan pembahasan mendalam mengenai Algoritma 2 yang lebih efisien.

## Algoritma 1: Pendekatan Iteratif
```python
def solution(number):
    if number < 0:
        return 0

    _sum = 0
    i = 3
    while i < number:
        _sum += i
        i += 3

    i = 5
    while i < number:
        if i % 3 == 0:
            i += 5
            continue
        _sum += i
        i += 5
    return _sum
```
Algoritma ini menggunakan pendekatan iteratif dengan loop untuk menghitung jumlah secara langsung. Kita memeriksa setiap bilangan dari 1 hingga `number - 1`, menambahkan bilangan tersebut ke dalam jumlah jika ia habis dibagi 3 atau 5. 

### Kompleksitas Algoritma

1. **Perulangan Pertama (`while i < number`) dengan `i` dimulai dari 3 dan bertambah 3 setiap iterasi**: Perulangan ini akan berjalan sekitar `number/3` kali. Kompleksitasnya adalah O(number/3), yang disederhanakan menjadi O(number).

2. **Perulangan Kedua (`while i < number`) dengan `i` dimulai dari 5 dan bertambah 5 setiap iterasi, kecuali ketika `i % 3 == 0`**: Perulangan ini akan berjalan sekitar `number/5` kali, dikurangi beberapa iterasi karena pengabaian bilangan yang habis dibagi 3. Kompleksitasnya adalah O(number/5), yang juga disederhanakan menjadi O(number).

Kedua loop tersebut berjalan secara independen dan tidak _nested_, sehingga kompleksitas total fungsi `solution` adalah O(number) + O(number) = O(number). Ini berarti waktu yang dibutuhkan untuk menjalankan algoritma meningkat linearly dengan besarnya nilai input. Meskipun algoritma ini mudah dipahami dan diimplementasikan, kompleksitas waktu linear membuatnya kurang efisien untuk nilai `number` yang sangat besar.

## Algoritma 2: Pendekatan Deret Aritmatika

```python
def solution(number):  # --> this is very clever way
    if number < 0:
        return 0

    a3 = (number-1)//3
    a5 = (number-1)//5
    a15 = (number-1)//15
    return (a3*(a3+1)//2)*3 + (a5*(a5+1)//2)*5 - (a15*(a15+1)//2)*15
```

Algoritma kedua menggunakan rumus deret aritmatika untuk menghitung jumlah bilangan yang habis dibagi 3 atau 5. Ini dilakukan dengan menghitung jumlah kelipatan 3 dan 5 di bawah `number`, lalu mengurangi jumlah kelipatan 15 untuk menghindari penghitungan ganda.

### Kompleksitas Algoritma

Kompleksitas waktu dari Algoritma 2 adalah O(1), artinya waktu eksekusi algoritma tidak tergantung pada nilai `number` dan tetap konstan. Ini jauh lebih efisien dibandingkan dengan Algoritma 1, terutama untuk nilai `number` yang besar.

### Pembahasan Mendalam tentang Algoritma 2

Algoritma 2 berdasarkan pada prinsip bahwa jumlah kelipatan suatu bilangan dalam rentang tertentu bisa dihitung dengan menggunakan rumus jumlah deret aritmatika. Ini memungkinkan kita untuk menghitung jumlah tanpa harus mengiterasi setiap bilangan.

## Intuisi dan Pendekatan Matematis

### 1. Mengidentifikasi Bilangan yang Habis Dibagi 3 atau 5

Tujuan utama adalah untuk menemukan jumlah semua bilangan yang habis dibagi 3 atau 5. Misalnya, jika `number` adalah 10, bilangan yang relevan adalah 3, 5, 6, dan 9.

### 2. Menggunakan Rumus Deret Aritmatika

Fungsi ini mengimplementasikan rumus jumlah deret aritmatika. Rumus umum untuk menemukan jumlah `n` suku pertama dari deret aritmatika adalah:

$$\frac{n}{2} \times (a_1 + a_n)$$

di mana $a_1$ adalah suku pertama dan $a_n$ adalah suku ke-n. Dalam konteks ini, deret tersebut adalah kelipatan 3, 5, dan 15.

### 3. Menghitung Kelipatan 3, 5, dan 15

- **Kelipatan 3**: Jumlah semua kelipatan 3 di bawah `number` dihitung dengan rumus:


  $$\frac{a3}{2} \times (3 + a3 \times 3)$$

  di mana `a3` adalah jumlah kelipatan 3.

- **Kelipatan 5**: Proses serupa diterapkan untuk kelipatan 5.

- **Kelipatan 15 (Pengurangan Duplikasi)**: Kelipatan 15 dikurangi untuk menghindari penghitungan ganda.

### 4. Menghindari Penghitungan Ganda

Penghitungan kelipatan 15 dua kali harus dihindari karena setiap kelipatan 15 juga merupakan kelipatan 3 dan 5.

### 5. Jumlah Akhir

Dengan menambahkan jumlah kelipatan 3 dan 5, kemudian mengurangi jumlah kelipatan 15, kita mendapatkan total yang diinginkan.

## Kesimpulan

Perbandingan antara kedua algoritma ini menunjukkan pentingnya memilih pendekatan yang tepat untuk masalah tertentu. Algoritma 2, dengan kompleksitas waktu O(1) dan penerapan konsep matematika, jauh lebih efisien dibandingkan dengan pendekatan iteratif Algoritma 1 yang memiliki kompleksitas waktu O(n). Ini menekankan bahwa, dalam pemrograman komputer, algoritma yang lebih efisien seringkali dapat dicapai dengan memanfaatkan prinsip-prinsip matematika dan ilmiah.