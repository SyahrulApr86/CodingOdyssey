`reduce` adalah sebuah fungsi dalam modul `functools` di Python yang digunakan untuk menerapkan
sebuah fungsi secara berulang-ulang kepada pasangan item dalam sebuah iterable
(seperti list atau tuple), sehingga menghasilkan satu nilai tunggal. Ini adalah bagian dari paradigma pemrograman fungsional dan
sangat berguna untuk melakukan perhitungan kumulatif atau penggabungan data.


1. **Fungsi Reducer**: Fungsi yang digunakan dengan `reduce` harus menerima dua argumen. Fungsi ini akan dipanggil berulang kali dengan dua argumen ini.
2. **Aplikasi Berulang**: Pada setiap langkah, `reduce` menerapkan fungsi reducer tersebut ke dua elemen dari iterable. Hasilnya disimpan dan digunakan sebagai salah satu input untuk langkah berikutnya.
3. **Pengurangan Iteratif**: Proses ini berlanjut hingga semua elemen di iterable telah diproses, menyisakan satu nilai akhir.

### Contoh Penggunaan:

Misalkan kita ingin menjumlahkan semua angka dalam sebuah list. Kita bisa menggunakan `reduce` bersama dengan fungsi penjumlahan.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15
```

Fungsi `reduce` mengambil dua argumen: sebuah fungsi dan sebuah iterable. Dalam kasus ini, fungsi yang digunakan adalah `lambda x, y: x + y` (fungsi penjumlahan), dan iterable adalah `numbers`.

Berikut adalah langkah-langkah bagaimana `reduce` bekerja pada list `numbers`:

1. **Inisialisasi**: `reduce` memulai dengan dua elemen pertama dari list, yaitu `1` dan `2` dalam kasus ini.

2. **Langkah Pertama**: Fungsi `lambda` diaplikasikan pada dua elemen ini: `lambda 1, 2` menghasilkan `3`. Sekarang, `reduce` memegang nilai `3` sebagai hasil sementara.

3. **Langkah Kedua**: Kemudian, `reduce` mengambil hasil sementara (`3`) dan elemen berikutnya dari list (`3`), dan menerapkan fungsi `lambda` pada keduanya: `lambda 3, 3` menghasilkan `6`. Sekarang, hasil sementaranya adalah `6`.

4. **Langkah Ketiga**: Langkah berikutnya melibatkan hasil sementara (`6`) dan elemen berikutnya dari list (`4`): `lambda 6, 4` menghasilkan `10`. Hasil sementara sekarang adalah `10`.

5. **Langkah Keempat**: Akhirnya, `reduce` mengambil hasil sementara (`10`) dan elemen terakhir dari list (`5`), dan menerapkan fungsi `lambda` pada keduanya: `lambda 10, 5` menghasilkan `15`. Ini adalah hasil akhir dari `reduce`.

Proses ini bisa divisualisasikan seperti berikut:

```
Langkah 1: [1, 2, 3, 4, 5] -> lambda 1, 2 -> 3
Langkah 2: [3, 3, 4, 5]    -> lambda 3, 3 -> 6
Langkah 3: [6, 4, 5]       -> lambda 6, 4 -> 10
Langkah 4: [10, 5]         -> lambda 10, 5 -> 15
```

Jadi, `reduce` mengurangi seluruh list menjadi satu nilai dengan menerapkan fungsi yang diberikan secara berulang-ulang. Di akhir proses, `sum_result` menjadi `15`, yang merupakan penjumlahan dari semua elemen dalam list `numbers`.
