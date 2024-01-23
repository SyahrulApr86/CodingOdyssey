
## Algoritma 1: Metode Iteratif

Algoritma pertama menggunakan pendekatan iteratif untuk menghitung akar digital.

### Cara Kerja:
1. **Konversi Angka ke List Digit**: Angka diubah menjadi list digitnya.
2. **Iterasi dan Penjumlahan**: Setiap digit dijumlahkan bersama-sama.
3. **Pengecekan dan Pengulangan**: Jika hasil penjumlahan lebih dari satu digit, proses diulangi dengan angka baru yang dihasilkan dari penjumlahan.
4. **Pengembalian Hasil**: Proses berlanjut sampai didapatkan satu digit, yang kemudian dikembalikan sebagai hasil.

## Algoritma 2: Metode Matematik

Tentu, saya akan menjelaskan secara lebih rinci mengenai Algoritma 2, yang menggunakan pendekatan matematika untuk menghitung akar digital, dan mengapa pendekatan ini efektif.

## Algoritma 2: Pendekatan Matematik (Modulo 9)

### Konsep Dasar:
Algoritma ini berdasarkan pada sifat-sifat matematis dari angka dalam sistem bilangan basis 9. Dalam matematika, terdapat konsep yang menyatakan bahwa jumlah digit suatu angka memiliki hubungan langsung dengan sisa pembagiannya oleh 9.

### Cara Kerja:
1. **Operasi Modulo 9**: Operasi pertama yang dilakukan adalah `n % 9`. Ini menghasilkan sisa dari pembagian `n` dengan 9. Dalam konteks akar digital, operasi ini mengurangi angka menjadi bentuk paling sederhananya dalam kaitannya dengan 9.
   
2. **Pengecekan untuk Kelipatan 9**: Jika hasil dari `n % 9` adalah 0 dan `n` sendiri bukan 0, ini berarti bahwa `n` adalah kelipatan 9. Dalam kasus seperti ini, akar digital sebenarnya adalah 9, bukan 0.

3. **Ekspresi Kondisional**: Ekspresi `n % 9 or n and 9` secara efektif menghandle dua situasi: ketika `n` bukan kelipatan 9, hasilnya adalah `n % 9`; ketika `n` adalah kelipatan 9, hasilnya adalah 9.

### Mengapa Ini Bekerja:
- **Sifat Bilangan Basis 9**: Dalam matematika, setiap angka dapat dianggap sebagai representasi sumatif dari angka-angka dalam basis 9. Misalnya, angka 18 dalam basis 10 adalah 9+9, yang jika dijumlahkan kembali menjadi 18, dan akar digitalnya adalah 9.
  
- **Pengurangan Modular**: Dengan mengambil `n % 9`, kita sebenarnya melakukan pengurangan modular, yang mengurangi angka ke bentuk paling sederhananya dalam kaitannya dengan 9. Ini berarti mengulang proses penjumlahan digit sampai kita mendapatkan satu digit, yang secara matematis setara dengan mengambil modulo 9 dari angka asli.

- **Kasus Khusus untuk Kelipatan 9**: Dalam kasus kelipatan 9, seperti 9, 18, 27, dst., sisa pembagian oleh 9 adalah 0. Namun, karena akar digital untuk kelipatan 9 sebenarnya adalah 9, algoritma perlu menghandle kasus ini secara terpisah. Ekspresi `or n and 9` efektif dalam menangani kasus ini.

### Contoh:
- Ambil angka 12345. Melakukan `12345 % 9` menghasilkan 6, yang adalah akar digitalnya.
- Ambil angka 18. Melakukan `18 % 9` menghasilkan 0, namun karena ini adalah kelipatan 9, akar digitalnya adalah 9.
