# Capstone-Manajemen-rental-mobil
# Manajemen Rental Mobil

Program **Manajemen Rental Mobil** ini adalah aplikasi berbasis terminal yang digunakan untuk mengelola ketersediaan mobil, penyewaan, pengembalian, serta penghapusan data mobil dan penyewa dalam bisnis rental mobil.

## Fitur Utama

1. **Ketersediaan Mobil**
   - Menampilkan seluruh data mobil berdasarkan tahun (diurutkan dari yang tertua ke termuda).
   - Menampilkan mobil yang tersedia.
   - Menampilkan mobil yang sedang disewa.

2. **Penyewaan dan Penambahan Unit**
   - Menambah data penyewa baru.
   - Menambah data mobil baru.

3. **Pengembalian dan Perubahan Data Unit**
   - Mengubah status mobil yang telah dikembalikan menjadi "Tersedia".
   - Mengubah data mobil yang ada (jenis, tahun, kondisi, tarif sewa, dan status).

4. **Hapus Data dan History Penghapusan**
   - Menghapus data penyewa yang sudah mengembalikan mobil.
   - Menghapus data mobil berdasarkan tahun.
   - Menampilkan dan membersihkan riwayat data yang dihapus.

## Cara Menggunakan Program

1. **Menjalankan Program**
   - Jalankan program dan Anda akan disajikan dengan **Menu Utama** yang terdiri dari beberapa pilihan: Ketersediaan Mobil, Penyewaan, Pengembalian, Hapus Data, dan Keluar.

2. **Navigasi Menu**
   - Pilih nomor yang sesuai dengan tindakan yang ingin dilakukan. Masukkan angka yang sesuai dengan pilihan pada setiap menu.

3. **Menambah Penyewa atau Mobil**
   - Untuk menambah penyewa atau mobil baru, Anda akan diminta memasukkan informasi yang diperlukan seperti NIK, nama penyewa, nomor HP, alamat, jenis mobil, tahun mobil, tarif sewa, dll.

4. **Mengembalikan Mobil**
   - Setelah penyewa mengembalikan mobil, status mobil akan diperbarui menjadi "Tersedia" melalui menu pengembalian.

5. **Riwayat Penghapusan**
   - Program juga menyimpan riwayat penghapusan data mobil dan penyewa, yang bisa ditampilkan atau dihapus dari sistem.

## Dependencies

Program ini menggunakan library **Tabulate** untuk menampilkan data dalam format tabel yang lebih rapi di terminal.

Instalasi Tabulate:
```bash
pip install tabulate
