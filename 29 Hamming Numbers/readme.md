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
## Pendekatan Menggunakan Queue dalam Menghasilkan Hamming Number

Kode yang disediakan di bawah ini menunjukkan pendekatan menggunakan queue untuk menemukan Hamming Number ke-N. Pendekatan ini memanfaatkan struktur data queue untuk efisien menghasilkan Hamming Numbers secara berurutan dengan mengurangi jumlah perhitungan yang tidak perlu.

### Kode

```python
from collections import deque

def hamming_queue(N):
    hamming_numbers = [1] * N
    q2, q3, q5 = deque([2]), deque([3]), deque([5])
    i2 = i3 = i5 = 0

    for i in range(1, N):
        next_hamming = min(q2[0], q3[0], q5[0])
        hamming_numbers[i] = next_hamming
        if next_hamming == q2[0]:
            i2 += 1
            q2.popleft()
            q2.append(hamming_numbers[i2] * 2)
        if next_hamming == q3[0]:
            i3 += 1
            q3.popleft()
            q3.append(hamming_numbers[i3] * 3)
        if next_hamming == q5[0]:
            i5 += 1
            q5.popleft()
            q5.append(hamming_numbers[i5] * 5)

    return hamming_numbers[-1]
```

Fungsi `hamming_queue` menggunakan tiga queue untuk mengelola kelipatan 2, 3, dan 5 dari Hamming Numbers yang telah dihasilkan. Pendekatan ini memungkinkan efisiensi yang lebih tinggi dalam menghasilkan Hamming Number ke-N dengan meminimalkan perhitungan yang berulang.

#### Cara Kerja Algoritma Menggunakan Queue

Algoritma untuk menghasilkan Hamming Number ke-N menggunakan queue bekerja dengan memanfaatkan struktur data queue untuk mengatur dan menghasilkan kelipatan 2, 3, dan 5 dari Hamming Numbers sebelumnya secara efisien. Berikut adalah penjelasan langkah demi langkah tentang cara kerjanya:

1. **Inisialisasi Queue dan Variabel**: Algoritma memulai dengan menginisialisasi tiga queue yang masing-masing akan menyimpan kelipatan 2 (`q2`), 3 (`q3`), dan 5 (`q5`) dari Hamming Numbers. Selain itu, array `hamming_numbers` diinisialisasi untuk menyimpan Hamming Numbers yang dihasilkan, dengan elemen pertama sudah diisi nilai 1, karena 1 adalah Hamming Number pertama.

2. **Menghasilkan Hamming Numbers Berikutnya**: Untuk setiap iterasi dari 1 hingga N-1 (karena Hamming Number pertama sudah diketahui), algoritma mencari nilai minimum dari elemen pertama pada masing-masing queue (`q2[0]`, `q3[0]`, `q5[0]`). Nilai minimum ini adalah Hamming Number berikutnya yang akan disimpan dalam array `hamming_numbers`.

3. **Memperbarui Queue**: Setelah menentukan Hamming Number berikutnya, algoritma memeriksa dari queue mana nilai minimum tersebut berasal. Jika nilai tersebut berasal dari `q2`, maka elemen pertama pada `q2` di-dequeue (dihapus), dan kelipatan berikutnya dari Hamming Number tersebut dengan 2 ditambahkan ke `q2`. Proses serupa dilakukan untuk `q3` dan `q5` dengan menggunakan faktor 3 dan 5, masing-masing.

4. **Pembaruan Indeks dan Penambahan Kelipatan Baru**: Untuk setiap queue yang elemennya telah di-dequeue, indeks yang sesuai (`i2` untuk `q2`, `i3` untuk `q3`, dan `i5` untuk `q5`) ditingkatkan. Ini menandakan bahwa telah diambil satu elemen dari queue tersebut, dan kelipatan baru dari Hamming Number di posisi indeks yang ditingkatkan tersebut dengan faktor masing-masing (2, 3, atau 5) ditambahkan ke dalam queue yang sesuai.

5. **Pengulangan Sampai N Terpenuhi**: Proses ini diulang hingga `hamming_numbers` telah diisi dengan N elemen. Hamming Number ke-N adalah elemen terakhir dalam array `hamming_numbers`.

Algoritma ini efektif karena setiap Hamming Number baru yang dihasilkan selalu merupakan kelipatan terkecil berikutnya yang mungkin dari 2, 3, atau 5 dari Hamming Numbers sebelumnya. Dengan menggunakan queue, algoritma memastikan bahwa semua Hamming Numbers dihasilkan dalam urutan yang benar tanpa perlu melakukan perhitungan ulang atau pengecekan bilangan yang tidak perlu. Ini mengurangi jumlah operasi yang diperlukan dan meningkatkan efisiensi, terutama dibandingkan dengan pendekatan naif yang memeriksa setiap bilangan satu per satu.

### Kompleksitas

#### Waktu

Pendekatan ini memiliki kompleksitas waktu yang lebih baik dibandingkan pendekatan naif. Kompleksitas waktu adalah O(N) karena setiap iterasi hanya memerlukan operasi dequeue dan enqueue yang berjalan dalam waktu konstan, serta operasi minimum yang juga efisien. Ini jauh lebih cepat untuk nilai N yang besar.

#### Ruang

Kompleksitas ruang untuk pendekatan ini juga O(N), terutama karena menyimpan N Hamming Numbers dalam array dan menggunakan struktur data tambahan (tiga queue) yang ukurannya bergantung pada N.

### Kelebihan dan Kekurangan

#### Kelebihan

- **Lebih Efisien**: Signifikan lebih efisien daripada pendekatan naif, terutama untuk nilai N yang besar.
- **Struktur Data yang Efektif**: Penggunaan queue memungkinkan manajemen kelipatan 2, 3, dan 5 yang efisien dan meminimalkan perhitungan yang tidak perlu.

#### Kekurangan

- **Memerlukan Pemahaman Lebih**: Pendekatan ini mungkin memerlukan pemahaman yang lebih mendalam tentang struktur data dan algoritma dibandingkan pendekatan naif.
- **Penggunaan Memori Lebih Besar**: Membutuhkan lebih banyak memori karena penggunaan queue dan penyimpanan intermediate Hamming Numbers.
---
## Pendekatan Menggunakan Heap dalam Menghasilkan Hamming Number

Kode yang disediakan di bawah ini menggunakan pendekatan heap (tumpukan) untuk menemukan Hamming Number ke-N. Pendekatan ini memanfaatkan struktur data heap untuk menyimpan dan mengelola kandidat Hamming Number secara efisien, sehingga meminimalisir waktu yang diperlukan untuk menemukan Hamming Number berikutnya dalam urutan.

### Kode

```python
import heapq

def hamming_heap(N):
    heap = [1]
    seen = {1}
    val = None

    for _ in range(N):
        val = heapq.heappop(heap)
        for factor in [2, 3, 5]:
            next_val = val * factor
            if next_val not in seen:
                heapq.heappush(heap, next_val)
                seen.add(next_val)

    return val
```

Fungsi `hamming_heap` menggunakan heap untuk menyimpan Hamming Numbers dan set `seen` untuk melacak bilangan yang sudah ditambahkan ke heap, guna menghindari duplikasi. Ini memungkinkan algoritma untuk secara efisien menemukan dan menyimpan Hamming Numbers dalam urutan yang benar tanpa perlu melakukan perhitungan berulang.

#### Cara Kerja Algoritma Menggunakan Heap

Algoritma menggunakan heap untuk menghasilkan Hamming Number ke-N bekerja dengan cara yang canggih dan efisien, memanfaatkan struktur data heap untuk menjaga kandidat Hamming Number dalam urutan terurut sambil menghindari duplikasi. Berikut adalah detail langkah demi langkah cara kerjanya:

1. **Inisialisasi Heap dan Set**: Algoritma dimulai dengan menginisialisasi heap yang berisi angka 1 (Hamming Number pertama) dan sebuah set `seen` untuk melacak bilangan yang sudah ditambahkan ke heap. Ini memastikan bahwa setiap Hamming Number yang dihasilkan unik.

2. **Pengulangan Untuk Menemukan N Hamming Numbers**: Untuk setiap iterasi dari 1 hingga N, algoritma melakukan beberapa operasi kunci:
   - **Pengambilan Minimum**: Menggunakan `heapq.heappop(heap)`, algoritma mengambil elemen terkecil dari heap, yang pada iterasi pertama akan selalu 1. Ini merupakan Hamming Number berikutnya dalam urutan.
   
   - **Penggandaan dan Penambahan Kembali ke Heap**: Untuk setiap faktor (2, 3, dan 5), algoritma mengalikan elemen yang baru diambil dengan faktor tersebut untuk mendapatkan kandidat Hamming Number berikutnya. Jika kandidat belum ada di dalam set `seen`, itu menandakan bahwa kandidat tersebut belum ditambahkan ke heap, maka:
     - Kandidat ditambahkan ke heap menggunakan `heapq.heappush(heap, next_val)`.
     - Kandidat juga ditambahkan ke set `seen` untuk melacak bahwa bilangan tersebut sudah diakui sebagai kandidat Hamming Number dan sudah ada dalam heap.

3. **Pencegahan Duplikasi**: Set `seen` memastikan bahwa setiap kandidat yang dihasilkan dan ditambahkan ke heap adalah unik, mencegah duplikasi dalam heap dan mengoptimalkan proses pencarian Hamming Number.

4. **Pengembalian Hamming Number ke-N**: Setelah loop mencapai iterasi ke-N, algoritma mengembalikan elemen terakhir yang diambil dari heap, yang merupakan Hamming Number ke-N.

#### Efisiensi Heap

Menggunakan heap memungkinkan algoritma untuk secara efisien menjaga kandidat Hamming Number dalam urutan terurut tanpa perlu melakukan sortasi manual setiap kali elemen baru ditambahkan. Operasi `heappop` dan `heappush` berjalan dalam waktu logaritmik terhadap ukuran heap, menjadikan penambahan dan pengambilan elemen sangat efisien.

#### Optimasi Dengan Set

Integrasi set `seen` dengan heap menjadikan algoritma ini sangat efektif dalam meminimalisir pengulangan pekerjaan dengan memastikan hanya kandidat unik yang diproses. Ini mengurangi jumlah total operasi yang diperlukan dan secara signifikan meningkatkan kecepatan pencarian Hamming Number ke-N dibandingkan dengan pendekatan yang lebih sederhana.

Secara keseluruhan, algoritma menggunakan heap untuk menghasilkan Hamming Number ke-N adalah pendekatan yang sangat efisien, memanfaatkan kecepatan dan efisiensi struktur data heap untuk menyelesaikan masalah dengan cepat dan efektif.

### Kompleksitas

#### Waktu

Pendekatan menggunakan heap memiliki kompleksitas waktu yang lebih baik dibandingkan dengan pendekatan naif atau queue, terutama karena operasi `heappop` dan `heappush` berjalan dalam waktu logaritmik terhadap jumlah elemen dalam heap. Kompleksitas waktu keseluruhan adalah O(N log N), dimana N adalah posisi Hamming Number yang dicari.

#### Ruang

Kompleksitas ruang dari algoritma ini adalah O(N) karena memerlukan penyimpanan untuk heap dan set `seen`. Heap akan menyimpan hingga N bilangan Hamming berbeda pada satu waktu, dan set `seen` digunakan untuk melacak bilangan yang telah dilihat.

### Kelebihan dan Kekurangan

#### Kelebihan

- **Efisiensi Waktu**: Algoritma heap memungkinkan penemuan Hamming Number ke-N dengan lebih cepat dan efisien dibandingkan pendekatan lainnya, terutama untuk nilai N yang besar.
- **Pengelolaan Memori yang Efektif**: Penggunaan heap meminimalkan kebutuhan akan perhitungan ulang dan menyimpan hanya bilangan yang diperlukan.

#### Kekurangan

- **Kompleksitas Implementasi**: Meskipun Python menyediakan modul `heapq` yang memudahkan penggunaan heap, pendekatan ini secara konseptual lebih kompleks dibandingkan dengan pendekatan naif atau queue.
- **Penggunaan Memori**: Meskipun efisien, pendekatan ini memerlukan penggunaan memori tambahan untuk set `seen`, yang mungkin menjadi pertimbangan untuk dataset yang sangat besar.

---
## Pendekatan Pemrograman Dinamis dalam Menghasilkan Hamming Number

Kode yang disediakan di bawah ini menggunakan pendekatan pemrograman dinamis (Dynamic Programming, DP) untuk menemukan Hamming Number ke-N. Pendekatan ini memanfaatkan penghitungan sebelumnya untuk menghasilkan bilangan selanjutnya secara efisien, mengurangi jumlah perhitungan yang tidak perlu.

### Kode

```python
def hamming_number_DP(N):
    hamming_numbers = [1] * N  # Inisialisasi array untuk menyimpan N Hamming numbers
    i2 = i3 = i5 = 0  # Indeks untuk kelipatan 2, 3, dan 5
    
    # Nilai awal untuk kelipatan 2, 3, dan 5
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    
    for i in range(1, N):
        # Hamming number berikutnya adalah minimum dari ketiga kelipatan
        next_hamming_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        hamming_numbers[i] = next_hamming_number
        
        # Update nilai kelipatan jika mereka telah digunakan
        if next_hamming_number == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = hamming_numbers[i2] * 2
        if next_hamming_number == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = hamming_numbers[i3] * 3
        if next_hamming_number == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = hamming_numbers[i5] * 5
    
    return hamming_numbers[-1]  # Mengembalikan Hamming number ke-N
```
#### Cara Kerja Algoritma Pemrograman Dinamis

Algoritma pemrograman dinamis (DP) untuk menghasilkan Hamming Number ke-N bekerja dengan memanfaatkan konsep menyimpan hasil perhitungan sebelumnya dan menggunakan mereka untuk menghitung hasil berikutnya secara efisien. Berikut adalah penjelasan langkah demi langkah tentang cara kerjanya:

1. **Inisialisasi**: Algoritma memulai dengan menginisialisasi array `hamming_numbers` dengan ukuran N, diisi dengan 1 pada posisi pertama, mengingat 1 adalah Hamming Number pertama. Selanjutnya, mendefinisikan tiga indeks `i2`, `i3`, dan `i5` yang masing-masing akan digunakan untuk mengakses elemen dalam `hamming_numbers` untuk menghitung kelipatan 2, 3, dan 5 selanjutnya.

2. **Menentukan Hamming Number Berikutnya**: Untuk setiap iterasi, algoritma menentukan Hamming Number berikutnya dengan mengambil nilai minimum dari `next_multiple_of_2`, `next_multiple_of_3`, dan `next_multiple_of_5`, yang masing-masing adalah kelipatan selanjutnya dari 2, 3, dan 5 berdasarkan indeks `i2`, `i3`, dan `i5`.

3. **Pembaruan Nilai Kelipatan**: Setelah menentukan Hamming Number berikutnya, algoritma memeriksa apakah nilai ini diperoleh dari kelipatan 2, 3, atau 5. Berdasarkan sumber nilai tersebut, algoritma akan meningkatkan indeks terkait (`i2` untuk 2, `i3` untuk 3, `i5` untuk 5) dan menghitung kelipatan 2, 3, atau 5 selanjutnya dengan mengambil nilai dari `hamming_numbers` pada indeks yang baru ditingkatkan dan mengalikannya dengan 2, 3, atau 5.

4. **Pengulangan hingga N Terpenuhi**: Proses ini diulang hingga seluruh `hamming_numbers` diisi, dengan setiap iterasi menambahkan Hamming Number berikutnya ke dalam array. Karena setiap Hamming Number baru bergantung pada nilai-nilai sebelumnya, pendekatan ini memastikan bahwa semua Hamming Numbers dihasilkan secara efisien tanpa perhitungan ulang yang tidak perlu.

5. **Mengembalikan Hamming Number ke-N**: Setelah loop selesai, Hamming Number ke-N, yang berada pada posisi terakhir dalam array `hamming_numbers`, dikembalikan sebagai hasil akhir dari fungsi.

#### Keefektifan Pemrograman Dinamis

Pendekatan DP sangat efektif untuk masalah seperti ini karena:
- **Menghindari Perhitungan Ulang**: Dengan menyimpan Hamming Numbers yang telah dihitung, algoritma menghindari perlu melakukan perhitungan ulang, secara signifikan meningkatkan efisiensi.
- **Memanfaatkan Hasil Sebelumnya**: Dengan menggunakan nilai yang telah dihitung untuk menghasilkan nilai berikutnya, algoritma meminimalkan jumlah operasi yang diperlukan untuk mencapai hasil akhir.

Pendekatan pemrograman dinamis ini menunjukkan bagaimana penyimpanan sederhana dari hasil perhitungan sebelumnya dapat dimanfaatkan untuk memecahkan masalah yang lebih kompleks dengan cara yang sangat efisien dan efektif.

### Kompleksitas

#### Waktu

Pendekatan pemrograman dinamis memiliki kompleksitas waktu O(N), yang sangat efisien karena hanya memerlukan satu iterasi melalui N untuk menghasilkan Hamming Number ke-N. Setiap iterasi melibatkan operasi perbandingan dan pemilihan yang sederhana, serta pembaruan indeks dan nilai kelipatan, yang semuanya berjalan dalam waktu konstan.

#### Ruang

Kompleksitas ruang dari algoritma ini juga O(N) karena memerlukan penyimpanan untuk array `hamming_numbers` sepanjang N, serta beberapa variabel tambahan untuk indeks dan nilai kelipatan.

### Kelebihan dan Kekurangan

#### Kelebihan

- **Efisiensi Tinggi**: Algoritma sangat efisien dalam hal waktu dan ruang, membuatnya ideal untuk menemukan Hamming Number ke-N untuk nilai N yang besar.
- **Mengurangi Perhitungan Berulang**: Dengan menyimpan hasil perhitungan sebelumnya, pendekatan DP menghindari perhitungan yang berulang, mempercepat proses pencarian.

#### Kekurangan

- **Membutuhkan Pemahaman Konsep DP**: Meskipun efektif, pendekatan ini memerlukan pemahaman tentang pemrograman dinamis, yang mungkin membutuhkan waktu untuk dipelajari oleh pemula.
