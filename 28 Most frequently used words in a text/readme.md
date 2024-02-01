Algoritma 1 dan Algoritma 2, yang bertujuan untuk menemukan tiga kata paling sering muncul dalam sebuah teks, menggunakan pendekatan yang berbeda untuk memproses dan menganalisis teks. Mari kita bahas masing-masing dari segi pendekatan dan kompleksitas.

### Algoritma 1

**Pendekatan:**
- Menggunakan iterasi manual melalui setiap karakter dalam teks.
- Memisahkan kata berdasarkan whitespace dan tanda baca (kecuali apostrof) menggunakan kondisi if-else.
- Mengumpulkan kata dalam bentuk lowercase untuk menghitung frekuensi muncul dengan menggunakan dictionary sederhana (`dict`).
- Mengabaikan kata yang hanya terdiri dari apostrof.
- Mengurutkan kata-kata berdasarkan frekuensi munculnya dan mengambil tiga teratas.

**Kompleksitas:**
- **Waktu:** O(n + m log m), dimana n adalah jumlah karakter dalam teks, dan m adalah jumlah kata unik. Iterasi melalui setiap karakter memerlukan O(n), dan pengurutan kata berdasarkan frekuensi menggunakan O(m log m) karena `sorted()` pada Python.
- **Memori:** O(m), karena menyimpan setiap kata unik dan frekuensinya dalam sebuah dictionary.

### Algoritma 2

**Pendekatan:**
- Menggunakan regular expression (`re.findall`) untuk menemukan semua kata yang cocok dengan pola tertentu (huruf dan apostrof) dalam satu langkah, secara langsung dan efisien.
- Menggunakan `Counter` dari modul `collections` untuk menghitung frekuensi kata secara otomatis dan efisien.
- Memfilter kata yang hanya terdiri dari apostrof setelah penghitungan.
- Menggunakan `most_common(3)` dari `Counter` untuk langsung mendapatkan tiga kata dengan frekuensi tertinggi.

**Kompleksitas:**
- **Waktu:** O(n + k), dimana n adalah jumlah karakter dalam teks, dan k adalah proses untuk menghitung frekuensi dan mengambil tiga kata teratas. `re.findall` sangat efisien dalam menemukan kata, dan `Counter` melakukan penghitungan frekuensi dalam waktu linear terhadap jumlah kata.
- **Memori:** O(m), sama dengan algoritma 1 dalam hal penyimpanan kata unik dan frekuensinya. Namun, karena menggunakan `Counter`, mungkin ada overhead tambahan untuk struktur data ini dibandingkan dengan dictionary sederhana.

**Kesimpulan:**
- Algoritma 2 cenderung lebih efisien dari segi waktu eksekusi karena memanfaatkan ekspresi reguler dan struktur data `Counter` yang dioptimalkan untuk tugas-tugas seperti ini.
- Kedua algoritma memiliki kompleksitas memori yang serupa, tetapi Algoritma 2 mungkin menggunakan memori lebih efisien karena direktur integrasi dengan fungsi Python yang dioptimalkan.
- Dari perspektif pengembangan, Algoritma 2 lebih mudah dibaca dan lebih pendek, memanfaatkan fungsi bawaan Python untuk mengurangi kompleksitas kode.