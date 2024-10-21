from tabulate import tabulate

# Data Mobil
data_mobil = [
    {'Kode': 77, 'Jenis': 'Toyota Avanza', 'Tahun': 2019, 'Kondisi': 'Seadanya', 'Tarif Sewa': 300000, 'Status': 'Disewa'},
    {'Kode': 23, 'Jenis': 'Honda Brio', 'Tahun': 2021, 'Kondisi': 'Baik', 'Tarif Sewa': 400000, 'Status': 'Disewa'},
    {'Kode': 80, 'Jenis': 'Toyota Innova', 'Tahun': 2023, 'Kondisi': 'Baik', 'Tarif Sewa': 600000, 'Status': 'Tersedia'},
    {'Kode': 51, 'Jenis': 'Daihatsu Luxio', 'Tahun': 2020, 'Kondisi': 'Baik', 'Tarif Sewa': 500000, 'Status': 'Tersedia'},
    {'Kode': 65, 'Jenis': 'Daihatsu Sigra', 'Tahun': 2018, 'Kondisi': 'Seadanya', 'Tarif Sewa': 250000, 'Status': 'Tersedia'}
]

# Data Penyewa
data_penyewa = [
    {'Kode': 71, 'NIK': '1234567890123456', 'Nama': 'Budi Santoso', 'No HP': '628123456789', 'Alamat': 'Jakarta', 'Jaminan': 'KTP', 'Unit': 'Toyota Avanza'},
    {'Kode': 22, 'NIK': '9876543210987654', 'Nama': 'Siti Aminah', 'No HP': '628987654321', 'Alamat': 'Bandung', 'Jaminan': 'SIM', 'Unit': 'Honda Brio'}
]


# Data Mobil yang sedang disewa
def mobil_sedang_disewa():
    mobil_disewa = []
    for mobil in data_mobil:
        if mobil['Status'] == 'Disewa':
            mobil_disewa.append(mobil)
    return mobil_disewa


# Fungsi untuk menampilkan data mobil berdasarkan status
def tampilkan_data(status):
    if status == '1':
        stok_mobil = []
        for mobil in data_mobil:
            if mobil['Status'] == 'Tersedia':
                stok_mobil.append(mobil)
        print("Mobil yang Tersedia:")
        print(tabulate(stok_mobil, headers='keys', tablefmt='fancy_grid'))
    elif status == '2':
        print("Mobil yang Sedang Disewa:")
        print(tabulate(mobil_sedang_disewa(), headers='keys', tablefmt='fancy_grid'))

# Fungsi untuk mendapatkan tahun dari data mobil
def ambil_tahun(mobil):
    return mobil['Tahun']

# Fungsi untuk menampilkan seluruh mobil yang di urutkan berdasarkan tahun
def urutkan_data_mobil():
    data_mobil_sorted = sorted(data_mobil, key=ambil_tahun)
    print('Data mobil berhasil diurutkan berdasarkan tahun (tertua ke termuda).')
    print(tabulate(data_mobil_sorted, headers='keys', tablefmt='fancy_grid'))

# Fungsi untuk mendapatkan tarif sewa dari sebuah mobil
def ambil_tarif(mobil):
    return mobil['Tarif Sewa']

# Fungsi menampilkan seluruh data mobil berdasarkan tarif terendah
def tampilkan_data_berdasarkan_tarif():
    data_mobil_sorted_by_tarif = sorted(data_mobil, key=ambil_tarif)
    print('Mobil berdasarkan tarif sewa terendah:')
    print(tabulate(data_mobil_sorted_by_tarif, headers='keys', tablefmt='fancy_grid'))

# Menu Ketersediaan Mobil
def menu_ketersediaan_mobil():
    while True:
        print('''
        ===== MENU KETERSEDIAAN MOBIL =====
        1. Menampilkan seluruh data mobil berdasarkan tahun
        2. Menampilkan seluruh data mobil berdasarkan tarif
        3. Menampilkan mobil yang tersedia
        4. Menampilkan mobil yang sedang disewa
        5. Kembali ke menu utama
        ''')
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            urutkan_data_mobil()
        elif pilihan == '2':
            tampilkan_data_berdasarkan_tarif()
        elif pilihan == '3':
            tampilkan_data('1')
        elif pilihan == '4':
            tampilkan_data('2')
        elif pilihan == '5':
            return
        else:
            print('Pilihan tidak valid, masukan angka antara 1,2,3,4,5')

# Fungsi input alfabet
def input_alfabet(prompt):
    while True:
        data = input(prompt)
        if data.replace(' ', '').isalpha():
            return data
        else:
            print('Data yang anda masukan harus berupa huruf, silahkan coba lagi.')

# Fungsi input digit
def input_digit(prompt):
    while True:
        nomor = input(prompt)
        if nomor.isdigit():
            return int(nomor)
        else:
            print('Data yang anda masukan harus berupa angka, silahkan coba lagi.')



# Fungsi untuk input NIK 16 digit
def input_nik(prompt):
    while True:
        NIK = input(prompt)
        if len(NIK) == 16 and NIK.isdigit():
            return NIK
        else:
            print("NIK harus 16 digit angka. Silakan coba lagi.")

# Fungsi input status mobil
def input_status():
    while True:
        status = input("Masukkan status mobil (Tersedia/Disewa): ").capitalize()
        if status == 'Tersedia':
            return 'Tersedia'
        elif status == 'Disewa':
            return 'Disewa'
        else:
            print("Status tidak valid. Harus 'Tersedia' atau 'Disewa'.")

# Fungsi menampilkan data penyewa
def tampilkan_data_penyewa():
    print(tabulate(data_penyewa, headers='keys', tablefmt='fancy_grid'))

# Fungsi menambah data penyewa
def tambah_data_penyewa():
    NIK = input_nik('Masukkan NIK penyewa(16 digit angka): ')
    Nama = input_alfabet('Masukkan nama penyewa: ')
    No_HP = input_digit('Masukkan nomor HP penyewa: ')
    Alamat = input_alfabet('Masukkan alamat penyewa: ')
    Jaminan = input_alfabet('Masukkan jaminan penyewa: ')

    while True:
        Unit = input_alfabet('Masukkan unit mobil yang ingin disewa: ')
        mobil_tersedia = False

        for mobil in data_mobil:
            if mobil['Jenis'].lower() == Unit.lower() and mobil['Status'] == 'Tersedia':
                mobil['Status'] = 'Disewa'
                kode_baru = max([penyewa['Kode'] for penyewa in data_penyewa]) + 1
                data_penyewa.append({'Kode': kode_baru, 'NIK': NIK, 'Nama': Nama, 'No HP': No_HP, 'Alamat': Alamat, 'Jaminan': Jaminan, 'Unit': mobil['Jenis'] })
                print('Data penyewa berhasil ditambahkan.')
                tampilkan_data_penyewa()
                print("Data mobil yang tersedia saat ini:")
                tampilkan_data('1')
                mobil_tersedia = True  # Menandakan mobil ditemukan dan status berubah
                break

        if mobil_tersedia:
            return
        else:
            print(f"Mobil {Unit} sedang disewa atau tidak tersedia. Silakan pilih mobil lain yang 'Tersedia'.")

# Fungsi menambah data mobil
def tambah_data_mobil():
    Jenis = input_alfabet('Masukkan jenis mobil: ')
    Tahun = input_digit('Masukkan tahun mobil: ')
    Kondisi = input_alfabet('Masukkan kondisi mobil: ')
    Tarif_sewa = input_digit('Masukkan tarif sewa: ')
    Status = input_status()
    kode_baru = max([data['Kode'] for data in data_mobil]) + 1
    data_mobil.append({'Kode': kode_baru, 'Jenis' : Jenis, 'Tahun' : Tahun, 'Kondisi' : Kondisi, 'Tarif Sewa' : Tarif_sewa, 'Status' : Status})
    urutkan_data_mobil()
    print('berhasil menambahkan data baru')
    return

# Menu Penyewaan Unit
def menu_penyewaan_unit():
    while True:
        print('''
        ===== MENU PENYEWAAN DAN PENAMBAHAN UNIT =====
        1. Tambah data penyewa
        2. Tambah data mobil
        3. Kembali ke menu utama
        ''')
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            tambah_data_penyewa()
        elif pilihan == '2':
            tambah_data_mobil()
        elif pilihan == '3':
            return
        else:
            print('Pilihan tidak valid, silahkan masukan angka antara 1,2,3')

# Fungsi untuk mengubah status mobil yang sedang disewa menjadi tersedia
def ubah_status_mobil():

  # Tampilkan tabel mobil yang sedang disewa
    print("Mobil yang Sedang Disewa:")
    mobil_disewa = mobil_sedang_disewa()
    if not mobil_disewa:
        print("Tidak ada mobil yang sedang disewa.")
        return

    print(tabulate(mobil_disewa, headers='keys', tablefmt='fancy_grid'))

    kode = input_digit('Masukkan kode mobil yang sudah di kembalikan untuk diubah statusnya: ')
    for mobil in mobil_disewa:
        if mobil['Kode'] == kode:
            mobil['Status'] = 'Tersedia'
            print(f"Mobil {mobil['Jenis']} berhasil dikembalikan dan statusnya sekarang Tersedia.")
            tampilkan_data('2')  # Tampilkan data mobil yang sedang disewa
            tampilkan_data('1')  # Tampilkan data mobil yang tersedia
            return
    print('Mobil tidak ditemukan.')

# Fungsi untuk merubah data mobil
def merubah_data_mobil():
    print("Data Mobil saat ini")
    urutkan_data_mobil()  # Menampilkan data mobil yang ada
    kode = input_digit('Masukkan kode mobil yang ingin dirubah: ')
    
    for data in data_mobil:
        if data['Kode'] == kode:  # Jika kode mobil ditemukan
            print(f'Data mobil pada kode yang anda pilih saat ini: {data}')
            
            # Meminta input data baru dari pengguna
            Jenis = input_alfabet('Masukkan jenis mobil: ')
            Tahun = input_digit('Masukkan tahun mobil: ')
            Kondisi = input_alfabet('Masukkan kondisi mobil: ')
            Tarif_sewa = input_digit('Masukkan tarif sewa: ')
            Status = input_status() 
            
            # Memperbarui data mobil
            data['Jenis'] = Jenis
            data['Tahun'] = Tahun
            data['Kondisi'] = Kondisi
            data['Tarif Sewa'] = Tarif_sewa
            data['Status'] = Status
            
            print("Data mobil berhasil dirubah.")
            urutkan_data_mobil()
            return
    
    # Jika kode mobil tidak ditemukan
    print(f"Mobil dengan kode {kode} tidak ditemukan.")
# Menu Pengembalian Unit
def menu_pengembalian_unit():
    while True:
        print('''
        ===== MENU PENGEMBALIAN DAN PERUBAHAN DATA UNIT =====
        1. Ubah status mobil yang sudah di kembalikan
        2. Ubah data mobil
        3. Kembali ke menu utama
        ''')
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            ubah_status_mobil()
        elif pilihan == '2':
            merubah_data_mobil()
        elif pilihan == '3':
            return
        else:
            print('Pilihan tidak valid, masukan angka antara 1,2,3')


# Fungsi untuk menghapus data penyewa yang sudah mengembalikan mobil
def hapus_data_penyewa():
    penyewa_yang_sudah_mengembalikan = []
    for penyewa in data_penyewa:
        for mobil in data_mobil:
            if mobil['Jenis'] == penyewa['Unit'] and mobil['Status'] == 'Tersedia':
                penyewa_yang_sudah_mengembalikan.append(penyewa)
                break
    if penyewa_yang_sudah_mengembalikan:
        penyewa = penyewa_yang_sudah_mengembalikan[0]
        data_penyewa.remove(penyewa)
        riwayat_hapus_penyewa.append(penyewa)
        print(f"Penyewa atas nama {penyewa['Nama']} berhasil dihapus.")
        print("Data penyewa saat ini:")
        tampilkan_data_penyewa()
    else:
        print('Tidak ada penyewa yang sudah mengembalikan mobil.')

# Fungsi untuk menghapus mobil yag sudah di urutan tahunnya
def hapus_mobil_tahun():
  # Tampilkan semua data mobil terlebih dahulu
    urutkan_data_mobil()

    kode = input_digit('Masukkan kode mobil yang ingin dihapus: ')
    mobil_yang_dihapus = []

    # Mengumpulkan mobil dengan tahun yang ingin dihapus
    for mobil in data_mobil:
        if mobil['Kode'] == kode:
            mobil_yang_dihapus.append(mobil)

    if mobil_yang_dihapus:
        for mobil in mobil_yang_dihapus:
            data_mobil.remove(mobil)
            riwayat_hapus_mobil.append(mobil)
        print(f"Mobil dengan Kode {kode} berhasil dihapus.")
        print("Data mobil yang tersisa saat ini:")
        urutkan_data_mobil()

    else:
        print(f"Tidak ada mobil dengan kode {kode}.")

# Riwayat data yang dihapus
riwayat_hapus_mobil = []
riwayat_hapus_penyewa = []
#fungsi untuk menampilkan riwayat penghapusan
def tampilkan_riwayat_hapus():
    if not riwayat_hapus_mobil and not riwayat_hapus_penyewa:
        print("Tidak ada riwayat data yang dihapus.")
        return

    print("Riwayat Data Mobil yang Dihapus:")
    print(tabulate(riwayat_hapus_mobil, headers='keys', tablefmt='fancy_grid'))

    print("\nRiwayat Data Penyewa yang Dihapus:")
    print(tabulate(riwayat_hapus_penyewa, headers='keys', tablefmt='fancy_grid'))
    # Fungsi untuk membersihkan seluruh riwayat penghapusan data
def bersihkan_riwayat_hapus():
    riwayat_hapus_mobil.clear()
    riwayat_hapus_penyewa.clear()
    print("Riwayat penghapusan data berhasil dibersihkan.")

# Menu Hapus Data
def menu_hapus_data():
    while True:
        print('''
        ===== MENU HAPUS DATA DAN HISTORY PENGHAPUSAN DATA=====
        1. Hapus data penyewa yang sudah mengembalikan mobil
        2. Hapus data mobil berdasarkan tahun
        3. Menampilkan history data yang di hapus
        4. Membersihkan history data yang di hapus
        5. Kembali ke menu utama
        ''')
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            hapus_data_penyewa()
        elif pilihan == '2':
            hapus_mobil_tahun()
        elif pilihan == '3':
            tampilkan_riwayat_hapus()
        elif pilihan == '4':
            bersihkan_riwayat_hapus()
        elif pilihan == '5':
            return
        else:
            print('Pilihan tidak valid, silahkan masukan angka antara 1,2,3,4,5')

# Menu Utama
def menu_utama():
    while True:
        print('''
        ===== MANAJEMEN RENTAL MOBIL =====

        1. KETERSEDIAAN MOBIL

        2. PENYEWAAN DAN PENAMBAHAN UNIT

        3. PENGEMBALIAN DAN PERUBAHAN DATA UNIT

        4. HAPUS DATA DAN HISTORY PENGHAPUSAN DATA

        5. KELUAR
        ''')
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            menu_ketersediaan_mobil()
        elif pilihan == '2':
            menu_penyewaan_unit()
        elif pilihan == '3':
            menu_pengembalian_unit()
        elif pilihan == '4':
            menu_hapus_data()
        elif pilihan == '5':
            print('Terima kasih telah menggunakan program ini.')
            break
        else:
            print('Pilihan tidak valid, silahkan masukan kembali angka antara 1,2,3,4,5')

# Menjalankan program
menu_utama()

