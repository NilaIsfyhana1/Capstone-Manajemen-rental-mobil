# Dictionary gejala dan rekomendasi obat
rekomendasi_obat = {
    "demam": "Parasetamol",
    "batuk": "Obat Batuk Sirup",
    "pilek": "Dekongestan",
    "sakit kepala": "Ibuprofen",
    "mual": "Antasida",
    "nyeri otot": "Paracetamol atau Ibuprofen"
}

# Selamat datang di program
print("Selamat datang di Program Rekomendasi Obat!")
print("Masukkan gejala yang Anda rasakan untuk mendapatkan rekomendasi obat.\n")

# Meminta gejala dari pengguna
gejala_pasien = input("Masukkan gejala yang Anda rasakan: ").lower()

# Mengecek gejala dan memberikan rekomendasi obat
if gejala_pasien in rekomendasi_obat:
    print(f"Rekomendasi obat untuk gejala '{gejala_pasien}' adalah : {rekomendasi_obat[gejala_pasien]}")
else:
    print("Maaf, gejala yang Anda masukkan tidak terdaftar. Silakan konsultasikan dengan apoteker atau dokter.")
