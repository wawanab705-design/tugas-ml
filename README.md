# Deskripsi Singkat :
Aplikasi Prediksi Biaya Belanja Pasien Rumah Sakit adalah sebuah sistem berbasis data yang digunakan untuk memperkirakan total biaya yang kemungkinan dikeluarkan pasien selama menjalani perawatan sesuai dengan berapa kali kedatangan pasien. Aplikasi ini memanfaatkan informasi seperti jenis layanan medis, lama rawat inap, intensitas rawat jalan, dan obat yang digunakan.

# 1.	Eksplorasi Data (EDA)
-	Membaca dataset csv.
-	Menampilkan struktur data, seperti jumlah baris, kolom, tipe data, dan sampel 3 baris pertama.
-	Dataset awal memiliki 12 kolom tanpa nama, semua bertipe object.
-	Menampilkan data mentah seperti id_transaksi, id_pasien, dokter, jenis_layanan, poli, biaya, dll.

# 2.	Data Preparation & Preprocessing
1.	Rename kolom
    Kolom-kolom diubah menjadi nama yang mudah dipahami, seperti: id_transaksi, id_pasien, dokter , dsb.

3.	Convert tanggal
    Kolom waktu dikonversi ke datetime.

4.	Feature Engineering
   Ekstraksi fitur waktu:
   - Bulan
   - hari_dlm_minggu
   - hari_dlm_bulan

4.	Label Encoding untuk data kategori
    Kolom: dokter, poli, jenis_layanan.

6.	Memilih fitur untuk model
    bulan, hari_dlm_minggu, hari_dlm_bulan, dokter_encoded, poli_encoded, jenis_layanan_encoded.

7.	Membersihkan target biaya
  	Target awal biaya masih berupa string format Indonesia seperti "503,000.00".
  	Maka dilakukan: hapus koma, konversi ke float, mengisi missing value jika ada.

# 3.	Pelatihan Model
-	Model 1 - Linear Regression
    - Fit pada data train
    - Hasil: model berhasil dilatih
-	Model 2 - Random Forest Regressor 
    - Fit pada data train
    - Juga berhasil dilatih

# 4.	Evaluasi Model
Model dievaluasi menggunakan metrik:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

# 5.	Simpan Model
Menyimpan model menggunakan pickle.
